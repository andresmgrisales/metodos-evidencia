# metodos-evidencia
Plataforma de divulgación científica, estadística, ciencia de datos y métodos de investigación.

## Control de cambios editoriales

Política aprobada el 25 de noviembre de 2026.

Los nombres oficiales de navegación, en el orden establecido y para todos los tamaños de pantalla, son:

1. Inicio
2. Radar científico
3. Datos bajo análisis
4. Estadística sin mitos
5. Experimenta
6. Contacto

Los nombres, el título y subtítulo del portal, la identidad gráfica y la estructura de navegación requieren aprobación expresa del responsable editorial antes de modificarse. La adaptación a dispositivos debe ajustar el diseño al texto, sin abreviar, sustituir ni ocultar nombres de secciones.

Las actualizaciones ordinarias de contenidos respetarán el protocolo editorial y su periodicidad vigente, preservarán las publicaciones anteriores en sus colecciones y no modificarán los elementos estructurales aprobados. No se cambia la periodicidad ni el flujo de aprobación mediante esta política.

Antes de publicar un cambio, comprobar los seis nombres y su orden en navegación móvil y de escritorio, revisar que las secciones y publicaciones previas se conservan, y verificar que el diff no incluye cambios estructurales no autorizados. Los cambios estructurales aprobados se registrarán en un commit separado con su justificación.

### Ajuste editorial autorizado · 25 de noviembre de 2026

- Inicio: se retira el bloque introductorio azul y se incorpora «Destacados de la semana», con título de cada publicación, sección de origen y enlace directo.
- Estadística sin mitos: queda temporalmente oculta del menú, portada y navegación pública; se conserva su nombre y contenido para una futura reactivación autorizada.
- Las cuatro tarjetas activas de Inicio conservan los nombres oficiales y usan iconos temáticos y tonalidades suaves diferenciadas. Recursos se presenta en una sola tarjeta.
- La portada puede actualizar sus destacados conforme al protocolo editorial vigente, sin sustituir los contenidos de las colecciones ni alterar nombres o estructura sin aprobación.

### Ajuste editorial autorizado · 26 de noviembre de 2026

- Título de la pestaña en Inicio: muestra el título completo del portal, «Métodos & Evidencia · Estadística, ciencia de datos y métodos de investigación», en lugar de «Inicio · Métodos & Evidencia». Así coincide con el título del HTML y con el que muestran los buscadores. Las demás secciones conservan el formato «Sección · Métodos & Evidencia».
- Recursos: se incorpora después de «Sobre el autor y editor» un recuadro de servicios de análisis de datos para que instituciones, empresas e investigadores soliciten una propuesta por correo (andresmgrisales@gmail.com). Incluye el botón «Copiar correo», que funciona aunque el dispositivo no tenga una aplicación de correo configurada. El recuadro se publicó primero en Inicio y el mismo día se trasladó a Recursos, junto al perfil y los canales de contacto del autor; Inicio vuelve a su versión anterior. No cambia los nombres, el orden ni la estructura de la navegación.
- Recursos pasa a llamarse **Contacto** en el menú (escritorio y móvil), en su tarjeta de Inicio y en su encabezado. Su ícono pasa a ser un sobre (✉) en el menú y en la tarjeta. Conserva su posición en el menú y su identificador interno (`?seccion=recursos`), para que los enlaces existentes sigan funcionando. La sección queda con «Sobre el autor y editor», el recuadro de servicios y «Sobre Métodos & Evidencia». Se retiran las tarjetas «Series oficiales del IPC», «Bibliografía y DOI», «Experimentos didácticos» y «Lecturas de inferencia estadística», porque esas fuentes ya se citan en cada artículo y en cada publicación.
- Experimenta: los experimentos se presentan como tarjetas cliqueables, con el mismo formato de «Datos bajo análisis». Cada tarjeta abre una vista propia (`?seccion=laboratorio&experimento=muestra`, `ipc` o `significancia`) con un botón para volver, una presentación de 100 a 150 palabras que desarrolla el tema y explica lo que se observa en el simulador, y el simulador correspondiente. Los simuladores, sus cálculos y sus notas metodológicas no cambian.
- Radar científico: las lecturas publicadas se presentan como tarjetas cliqueables, con el mismo formato de «Datos bajo análisis», bajo el rótulo «Lecturas publicadas». Cada tarjeta abre la página propia del artículo en `articulos/`. La lectura sobre agentes de IA incorpora el enlace «← Volver al Radar científico», como ya lo tenía la lectura del valor p. Se conservan las tres áreas editoriales y la nota sobre cómo se interpretan las lecturas.

### Auditoría de uniformidad y navegación · 26 de noviembre de 2026

Criterios adoptados para todo el sitio:

- **Rótulos:** cada publicación indica su colección, su número y su tema: «Datos bajo análisis · Análisis 01 · IPC», «Radar científico · Lectura 02 · Estadística y sus usos», «Experimenta · Experimento #001 · Muestreo». Los análisis se numeran 01 (IPC), 02 (Inferencia) y 03 (GEIH), y las lecturas del Radar 01 y 02.
- **Navegación de las publicaciones:** arriba, el nombre del portal y «← Volver a [colección]»; las páginas independientes repiten el regreso al final. Inflación y Significancia conservan además el menú del sitio.
- **Flechas:** → para páginas del sitio y ↗ solo para sitios externos.
- **Cierre de los análisis:** una caja «Para seguir explorando» con enlaces a contenidos relacionados que existen y están visibles.

Cambios aplicados:

- Se retiran los botones que llevaban a «Estadística sin mitos», que está oculta, y los sustituyen enlaces al experimento correspondiente y a la lectura del valor p.
- Se retiran el aviso «Nueva publicación» y los enlaces «Inflación · Significancia · Desempleo» de las páginas de análisis, y en la lectura de agentes de IA los enlaces «Inicio», «Lectura completa», «Explorar la lectura y la infografía» y «Conocer el observatorio», que repetían destinos o confundían.
- «Datos bajo análisis» usa el nombre de la sección como título, igual que las demás, y sus tarjetas describen cada análisis para el lector, en lugar de notas internas como «Contenido existente».
- La lectura de agentes de IA deja «Lectura inaugural» y «Laboratorio Académico de IA» y se alinea con los rótulos del Radar. El análisis de desempleo agrega el nombre del portal arriba y el regreso al final.
- El mapa del sitio actualiza sus fechas.

### Plantilla común de las publicaciones · 26 de noviembre de 2026

Todas las publicaciones de `analisis/` y `articulos/` comparten el mismo marco: el menú lateral de la página principal (arriba en el celular, con las cinco secciones completas y la sección activa resaltada), «← Volver a [colección]» arriba y al final, y el pie con perfiles y contador de visitas. El marco está en `css/marco.css` y sus clases llevan el prefijo `mx-`, para no chocar con los estilos propios de cada publicación.

- Inflación y Significancia dejan de ser copias completas de la página principal: pasan de unos 120 KB a 15 y 21 KB. Conservan su contenido, su encabezado (metadatos y vista previa al compartir) y solo el JavaScript de su gráfico o simulador, copiado literalmente de la versión anterior. Sus estilos de contenido están en `css/analisis.css`. Se verificó que se ven igual, píxel a píxel, y que el gráfico y el simulador producen exactamente los mismos resultados.
- Desempleo y las dos lecturas del Radar conservan su contenido, sus estilos y sus scripts; solo se sustituyen su navegación y su pie por el marco común.
- `herramientas/prerender.py` procesa ahora solo `index.html`, porque las publicaciones ya traen su contenido escrito en el HTML.

## Plantilla de las publicaciones

Para crear un análisis o una lectura nueva:

1. Copiar `herramientas/plantilla-publicacion.html` en `analisis/` (Datos bajo análisis) o `articulos/` (Radar científico), con un nombre descriptivo en minúsculas y con guiones.
2. Completar los metadatos (título, descripción, dirección canónica y Open Graph) y quitar la línea `noindex`.
3. En el menú lateral, marcar como activa la sección correspondiente y ajustar los dos enlaces «← Volver a …».
4. Escribir el contenido con la estructura de las demás publicaciones: rótulo (colección · número · tema), pregunta como título, entradilla, línea de datos, secciones, alcances y límites, fuentes y cierre «Para seguir explorando».
5. Agregar la tarjeta en su colección dentro de `index.html` (y en «Destacados de la semana», si corresponde), añadir la dirección a `sitemap.xml` y ejecutar `herramientas/prerender.py`.

Si cambian los nombres o el orden del menú, el cambio se hace en `navItems` de `index.html` y en la barra lateral de cada publicación y de la plantilla, que tienen los mismos cinco enlaces.
