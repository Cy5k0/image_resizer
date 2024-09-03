# Image Resizer Script

Este script permite redimensionar imágenes utilizando OpenCV. Puedes escalar la imagen según un porcentaje o especificar dimensiones específicas. El script también guarda la imagen redimensionada en una carpeta especificada con una calidad ajustada.

## Funciones

### `resize_image(image_path, scale_percent=None, width=None, height=None)`

Redimensiona una imagen basada en un porcentaje de escala o dimensiones específicas.

- **Args:**
  - `image_path` (str): Ruta de la imagen de entrada.
  - `scale_percent` (int, opcional): Porcentaje para escalar la imagen. Por defecto es None.
  - `width` (int, opcional): Nuevo ancho de la imagen en píxeles. Por defecto es None.
  - `height` (int, opcional): Nueva altura de la imagen en píxeles. Por defecto es None.
- **Returns:**
  - `numpy.ndarray`: Imagen redimensionada.

### `save_image(image, output_folder, output_filename, quality=90)`

Guarda una imagen en una carpeta especificada con una calidad dada.

- **Args:**
  - `image` (numpy.ndarray): Imagen a guardar.
  - `output_folder` (str): Carpeta donde se guardará la imagen.
  - `output_filename` (str): Nombre del archivo de salida.
  - `quality` (int, opcional): Calidad de la imagen guardada (1-100). Por defecto es 90.
- **Returns:**
  - None

## Variables Importantes

- `image_path`: Ruta de la imagen de entrada.
- `output_folder`: Carpeta donde se guardará la imagen redimensionada.
- `output_filename`: Nombre del archivo de salida.
- `scale_percent`: Porcentaje para escalar la imagen.
- `width`: Nuevo ancho de la imagen en píxeles.
- `height`: Nueva altura de la imagen en píxeles.
- `quality`: Calidad de la imagen guardada.

## Ejecución en Windows 10/11 y Linux

### Requisitos

- Python 3.x
- OpenCV

### Instalación de OpenCV

```bash
pip install opencv-python
```

## Futuro Desarrollo
Este script está diseñado para ser implementado en una futura aplicación web, donde los usuarios podrán redimensionar y guardar imágenes directamente desde su navegador

