import cv2
import numpy as np

def super_resolve_image(input_image_path, output_image_path, scale_factor=4):
    # Cargar el modelo ESPCN preentrenado
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    model_path = 'ESPCN_x2.pb'  # Asegúrate de descargar el modelo desde OpenCV's GitHub
    sr.readModel(model_path)
    sr.setModel('espcn', scale_factor)

    # Leer la imagen de entrada
    image = cv2.imread(input_image_path)
    if image is None:
        raise ValueError(f"No se pudo cargar la imagen en la ruta: {input_image_path}")

    # Mejorar la resolución de la imagen
    result = sr.upsample(image)

    # Guardar la imagen de salida
    cv2.imwrite(output_image_path, result)

# Rutas de la imagen de entrada y de salida
input_image_path = '/home/chsrueda/diginvasiveproject/Imágenes Visor/Sin título.png'
output_image_path = '/home/chsrueda/diginvasiveproject/Imágenes Visor/alta res Sin título.png'

# Ejecutar la función para mejorar la resolución
super_resolve_image(input_image_path, output_image_path, scale_factor=2)
