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
