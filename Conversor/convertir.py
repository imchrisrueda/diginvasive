import os
from PIL import Image
import pyheif

def heic_to_jpg(input_path, output_path):
    # Abrir el archivo HEIC
    heif_file = pyheif.read(input_path)
    
    # Convertir a formato de imagen compatible con PIL
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    
    # Guardar la imagen en formato JPG
    image.save(output_path, "JPEG")

def convert_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".heic"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".jpg")
            heic_to_jpg(input_file, output_file)
            print(f"Converted {input_file} to {output_file}")

# Ejemplo de uso:
input_directory = '/home/chsrueda/diginvasiveproject/Conversor/raw'
output_directory = '/home/chsrueda/diginvasiveproject/Conversor/JPG'
convert_directory(input_directory, output_directory)
