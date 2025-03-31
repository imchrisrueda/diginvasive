import cv2
import numpy as np

def remove_background(image_path, output_path):
    # Leer la imagen
    image = cv2.imread(image_path)
    # Convertir a espacio de color RGBA para incluir canal alpha
    image_rgba = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

    # Definir el rango de color para el fondo que quieres eliminar
    # Este rango se centra en colores claros y evita el negro y colores muy oscuros
    # Ajusta estos valores según el color específico de tu fondo
    lower = np.array([220, 220, 220, 255], dtype = "uint8")
    upper = np.array([255, 255, 255, 255], dtype = "uint8")

    # Crear una máscara que identifique el área del fondo
    mask = cv2.inRange(image_rgba, lower, upper)

    # Hacer que el fondo identificado por la máscara sea transparente
    image_rgba[mask > 0] = (0, 0, 0, 0)

    # Guardar la imagen resultante
    cv2.imwrite(output_path, image_rgba)

# Uso de la función
image_path = '/home/chsrueda/diginvasiveproject/WP/resources/diginvasive_font.PNG'
output_path = '/home/chsrueda/diginvasiveproject/WP/resources/diginvasive_no_background.png'

remove_background(image_path, output_path)
