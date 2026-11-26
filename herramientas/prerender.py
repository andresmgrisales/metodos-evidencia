"""Pre-renderiza el contenido inicial de <main id="page"> en las páginas que lo generan con JavaScript.

Por qué: los buscadores y las vistas previas de redes sociales que no ejecutan JavaScript
ven <main> vacío. Este script abre cada página en Chrome sin interfaz, toma el HTML que
genera el propio sitio y lo deja escrito dentro de <main>. Al cargar la página, el script
del sitio lo reemplaza por el mismo contenido, así que para el lector no cambia nada.

Uso (después de cualquier cambio en el contenido de esas páginas):
    pip install playwright && playwright install chromium
    python herramientas/prerender.py
"""
import asyncio, pathlib, re
from playwright.async_api import async_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ["index.html",
         "analisis/inflacion-y-nivel-de-precios.html",
         "analisis/significancia-estadistica-e-importancia.html"]
MAIN_RE = re.compile(r'(<main id="page" tabindex="-1">)(.*?)(</main>)', re.S)
import os
LAUNCH = {"executable_path": os.environ["CHROME_PATH"], "args": ["--no-sandbox"]} if os.environ.get("CHROME_PATH") else {}
MARK = '<!-- Contenido pre-renderizado (herramientas/prerender.py); el script del sitio lo regenera al cargar. -->\n'

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(**LAUNCH)
        ctx = await browser.new_context(viewport={"width": 1280, "height": 900})
        # Solo archivos locales: evita registrar visitas o depender de la red.
        await ctx.route("**/*", lambda r: r.abort() if not r.request.url.startswith("file://") else r.continue_())
        for rel in PAGES:
            path = ROOT / rel
            src = path.read_text(encoding="utf-8")
            assert len(MAIN_RE.findall(src)) == 1, f"{rel}: no se encontró un único <main id=\"page\">"
            # Se renderiza desde una copia con <main> vacío para no partir de un pre-renderizado viejo.
            clean = MAIN_RE.sub(r"\1\3", src)
            tmp = path.with_name(".prerender-" + path.name)
            tmp.write_text(clean, encoding="utf-8")
            try:
                page = await ctx.new_page()
                await page.goto(tmp.as_uri())
                await page.wait_for_timeout(500)
                inner = await page.eval_on_selector("#page", "el => el.innerHTML")
                await page.close()
            finally:
                tmp.unlink()
            out = MAIN_RE.sub(lambda m: m.group(1) + inner + m.group(3), clean)
            if MARK not in out:
                out = out.replace('<main id="page" tabindex="-1">', MARK + '<main id="page" tabindex="-1">', 1)
            path.write_text(out, encoding="utf-8")
            print(f"{rel}: {len(inner):,} caracteres pre-renderizados")
        await browser.close()

asyncio.run(main())
