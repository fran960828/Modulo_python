```python
# ====================================================================================================
# DOCUMENTACIÓN DE WEB SCRAPING CON BEAUTIFUL SOUP Y REQUESTS
# ====================================================================================================

# Este script demuestra cómo utilizar las librerías 'requests' y 'beautifulsoup4'
# para extraer información específica (títulos, resúmenes y enlaces de videos)
# de un sitio web, y cómo guardar esa información en un archivo CSV.
# El proceso se conoce como Web Scraping.

# NOTA PARA PRINCIPIANTES: Antes de ejecutar, asegúrese de tener instaladas las librerías necesarias.
# Se recomienda instalar Beautiful Soup 4 y el analizador LXML, además de Requests.
# Puede instalarlas usando pip en su terminal:
# pip install beautifulsoup4
# pip install lxml
# pip install requests

# ====================================================================================================
# PASO 1: Importar Librerías Necesarias
# ====================================================================================================

# Importamos 'requests' para hacer la solicitud web y obtener el código fuente HTML.
import requests

# Importamos 'BeautifulSoup' para analizar y navegar por el HTML.
# 'bs4' es el nombre común del módulo Beautiful Soup 4.
from bs4 import BeautifulSoup

# Importamos 'csv' para guardar la información extraída de forma estructurada.
import csv

# ====================================================================================================
# PASO 2: Obtener el Código Fuente (HTML)
# ====================================================================================================

# Utilizamos la librería 'requests' para acceder a la página web objetivo.
# Esto nos devuelve un objeto de respuesta (response object).
# La URL utilizada es el sitio web de ejemplo del video.
# Solicitamos la página y añadimos '.text' al final para obtener solo el código fuente HTML como un string.
try:
    source = requests.get('http://coreyms.com').text
except Exception as e:
    # Manejo básico de errores si la solicitud falla
    print(f"Error al obtener el código fuente: {e}")
    exit()

# ====================================================================================================
# PASO 3: Crear el Objeto Beautiful Soup (Análisis del HTML)
# ====================================================================================================

# Creamos el objeto 'soup' de Beautiful Soup.
# Le pasamos el código fuente obtenido ('source').
# Es crucial especificar el analizador (parser); utilizamos 'lxml', que es recomendado.
soup = BeautifulSoup(source, 'lxml')

# ====================================================================================================
# PASO 4: Preparar el Archivo CSV para Guardar los Datos
# ====================================================================================================

# Abrimos el archivo CSV. Lo llamamos 'cms_scrape.csv'.
# Usamos 'w' para indicar que vamos a escribir (write) en él.
# NOTA: En un contexto real, se recomienda usar un context manager 'with open(...)'
csv_file = open('cms_scrape.csv', 'w')

# Creamos un objeto 'writer' para escribir filas de datos en el archivo CSV.
csv_writer = csv.writer(csv_file)

# Escribimos la fila de encabezados (nombres de columna) para el CSV.
# Los encabezados serán: 'headline', 'summary' y 'video_link'.
csv_writer.writerow(['Headline', 'Summary', 'Video Link'])

# ====================================================================================================
# PASO 5: Localizar y Extraer Múltiples Elementos (Artículos)
# ====================================================================================================

# Queremos extraer la información de todos los artículos de la página.
# Usamos el método '.find_all()' en lugar de '.find()' porque esperamos múltiples resultados.
# '.find_all()' devuelve una lista de todas las etiquetas que coinciden con los criterios.
# En el sitio de ejemplo, cada publicación principal está contenida dentro de una etiqueta <article>.
# Iteramos sobre esta lista de artículos.
for article in soup.find_all('article'):

    # --------------------------------------------------------------------------------
    # A. Extracción del Titular (Headline)
    # --------------------------------------------------------------------------------

    # Buscamos el titular dentro del artículo actual (no en todo el 'soup').
    # El titular está anidado: dentro de una etiqueta <h2>, que contiene un enlace <a>.
    # Accedemos a las etiquetas como atributos, y luego usamos .text para obtener solo el contenido de texto.
    try:
        headline = article.h2.a.text
    except:
        # Si el titular falta (aunque es improbable), asignamos 'None'
        headline = None

    # --------------------------------------------------------------------------------
    # B. Extracción del Resumen (Summary)
    # --------------------------------------------------------------------------------

    # El resumen está en un párrafo (<p>) dentro de un div con una clase específica: 'entry-content'.
    # Para encontrar un div con una clase específica, usamos el método '.find()'.
    # NOTA: En Python, usamos 'class_' con guion bajo, ya que 'class' es una palabra reservada.
    try:
        # Buscamos el div contenedor del contenido.
        entry_content = article.find('div', class_='entry-content')
        
        # Luego, dentro de ese div, buscamos el primer párrafo y extraemos su texto.
        summary = entry_content.p.text
    except:
        summary = None


    # --------------------------------------------------------------------------------
    # C. Extracción del Enlace de Video (La parte más compleja)
    # --------------------------------------------------------------------------------

    # La extracción de la URL del video es compleja porque requiere obtener el atributo 'src'
    # de un iframe y luego manipular esa cadena para obtener el ID del video.

    # Inicializamos la variable que contendrá el enlace de YouTube.
    youtube_link = None 

    # Implementamos un bloque try/except. Esto es esencial.
    # Si un artículo no tiene video, el intento de buscar el iframe fallará y romperá el script.
    # El bloque try/except asegura que, si falla, asignemos un valor (None) y continuemos con el siguiente artículo.
    try:
        # 1. Encontrar el iframe: Buscamos un iframe con la clase 'youtube-player'.
        iframe = article.find('iframe', class_='youtube-player')
        
        # 2. Obtener el atributo 'src': No queremos el texto, queremos el valor del atributo 'src'.
        # Accedemos a los atributos de la etiqueta como si fuera un diccionario.
        vid_source = iframe['src']

        # 3. Parsear la URL (Obtener el ID del video): El ID del video es el quinto elemento
        # después de dividir la cadena por '/' (índice 4).
        vid_id_with_params = vid_source.split('/')

        # 4. Eliminar parámetros de consulta: El ID aún contiene parámetros que comienzan con '?'.
        # Dividimos la cadena usando '?' y tomamos el primer elemento (índice 0), que es el ID puro.
        vid_id = vid_id_with_params.split('?')

        # 5. Reconstruir el Enlace de YouTube: Creamos un enlace limpio y estándar de YouTube con el ID.
        youtube_link = f'https://youtube.com/watch?v={vid_id}'
        
    except Exception as e:
        # Si la búsqueda falla (porque no hay video), entramos aquí.
        # Asignamos 'None' a la variable y el script continúa.
        youtube_link = None


    # --------------------------------------------------------------------------------
    # D. Imprimir y Guardar Resultados
    # --------------------------------------------------------------------------------

    # Imprimimos la información extraída en la terminal.
    print(f"Título: {headline}")
    print(f"Resumen: {summary}")
    print(f"Enlace de Video: {youtube_link}")
    print() # Para separar los artículos en la salida.

    # Escribimos los datos del artículo actual en una nueva fila del archivo CSV.
    csv_writer.writerow([headline, summary, youtube_link])

# ====================================================================================================
# PASO 6: Cerrar el Archivo CSV
# ====================================================================================================

# Una vez que el bucle ha terminado y todos los datos han sido guardados, cerramos el archivo.
csv_file.close()

# Nota: Se debe ser considerado al hacer web scraping y evitar enviar demasiadas solicitudes
# rápidamente a un servidor para no sobrecargarlo. Algunos sitios grandes ofrecen APIs públicas.