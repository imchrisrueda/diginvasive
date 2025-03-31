import cv2
import numpy as np
from skimage import measure
import svgwrite

def remove_background_and_generate_svg(image_path, output_svg_path):
    # Cargar la imagen
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"No se pudo cargar la imagen en la ruta: {image_path}")

    # Convertir a escala de grises y aplicar umbral
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

    # Invertir los colores
    inverted_thresh = cv2.bitwise_not(thresh)

    # Encontrar los contornos
    contours = measure.find_contours(inverted_thresh, 0.8)

    # Crear un nuevo documento SVG
    dwg = svgwrite.Drawing(output_svg_path, profile='tiny')

    # Añadir los contornos al SVG
    for contour in contours:
        points = [(point[1], point[0]) for point in contour]
        dwg.add(dwg.polygon(points, fill='none', stroke='black'))

    # Guardar el SVG
    dwg.save()

# Ruta de la imagen de entrada y el archivo SVG de salida
image_path = '/home/chsrueda/diginvasiveproject/WP/resources/diginvasive_font.jpg'
output_svg_path = '/home/chsrueda/diginvasiveproject/WP/resources/diginvasive_font_nb.svg'

# Ejecutar la función
remove_background_and_generate_svg(image_path, output_svg_path)
