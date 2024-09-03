import cv2
import os

def resize_image(image_path, scale_percent=None, width=None, height=None):
    """
    Resize an image based on a scale percentage or specific dimensions.

    Args:
        image_path (str): Path to the input image.
        scale_percent (int, optional): Percentage to scale the image. Defaults to None.
        width (int, optional): New width of the image in pixels. Defaults to None.
        height (int, optional): New height of the image in pixels. Defaults to None.

    Returns:
        numpy.ndarray: Resized image.
    """
    image = cv2.imread(image_path)
    original_height, original_width = image.shape[:2]
    
    if scale_percent:
        width = int(original_width * scale_percent / 100)
        height = int(original_height * scale_percent / 100)
    elif width and height:
        pass
    else:
        width = original_width
        height = original_height

    resized_image = cv2.resize(image, (width, height), interpolation=cv2.INTER_AREA)
    return resized_image

def save_image(image, output_folder, output_filename, quality=90):
    """
    Save an image to a specified folder with a given quality.

    Args:
        image (numpy.ndarray): Image to be saved.
        output_folder (str): Folder to save the image.
        output_filename (str): Name of the output file.
        quality (int, optional): Quality of the saved image (1-100). Defaults to 90.

    Returns:
        None
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    output_path = os.path.join(output_folder, output_filename)
    
    if output_filename.lower().endswith('.jpg') or output_filename.lower().endswith('.jpeg'):
        cv2.imwrite(output_path, image, [cv2.IMWRITE_JPEG_QUALITY, quality])
    else:
        cv2.imwrite(output_path, image)
    
    print(f"Imagen guardada en {output_path} con calidad {quality}")

# Estas rutas podrían ser entregadas por el usuario , pero el fin de esto es usarlo desde una app web
image_path = 'perro.jpg'
output_folder = './img_escalada'

print("Seleccione el tipo de escalado:")
print("1. Escalar por porcentaje")
print("2. Especificar ancho y alto en píxeles")
choice = int(input("Ingrese 1 o 2: "))

if choice == 1:
    scale_percent = int(input("Ingrese el porcentaje de escalado (por ejemplo, 50 para reducir al 50%): "))
    resized_image = resize_image(image_path, scale_percent=scale_percent)
elif choice == 2:
    width = int(input("Ingrese el nuevo ancho en píxeles: "))
    height = int(input("Ingrese la nueva altura en píxeles: "))
    resized_image = resize_image(image_path, width=width, height=height)
else:
    print("Opción no válida.")
    exit()

output_filename = input("Ingrese el nombre del archivo de salida (incluya la extensión, por ejemplo, 'imagen_escalada.jpg'): ")

if output_filename.lower().endswith('.jpg') or output_filename.lower().endswith('.jpeg'):
    quality = int(input("Ingrese la calidad de la imagen (1-100, donde 100 es la mejor calidad): "))
else:
    quality = 90

save_image(resized_image, output_folder, output_filename, quality=quality)
