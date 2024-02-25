# ProyectIP
 This project aims to learn the use of OpenCV and work with the camera, the objective is to simulate the vision of different animals.

## Need to download:
pygames
cv2

# Documentación de "Animal Sight"
### Introducción
El proyecto "Animal Sight" es una aplicación de visualización que simula la visión de diferentes animales. Utiliza la biblioteca Pygame para la interfaz gráfica, OpenCV para el procesamiento de imágenes y NumPy para manipular matrices.

## Estructura del Proyecto
El proyecto se divide en dos archivos principales:

mainGUI.py: Este archivo contiene la interfaz gráfica del programa. Se encarga de la inicialización de Pygame, maneja la interfaz del usuario y llama a las funciones de transformación de imágenes según la opción seleccionada.

mainCode.py: Contiene funciones que realizan las transformaciones de imágenes según la visión de diferentes animales. Estas funciones son llamadas desde mainGUI.py para generar las visualizaciones.

## mainGUI.py
### Inicialización y Configuración
pygame.init(): Inicializa la biblioteca Pygame.
Definición de colores y configuración de pantalla: Define los colores y el tamaño de la pantalla.
Variables Globales
animal_sight_type: Representa el tipo de visión del animal actualmente seleccionado.
animals: Lista de tipos de animales disponibles.
menu_active: Indica si se encuentra en el menú principal.
menu_option: Almacena la opción del menú seleccionada.
section_active: Indica si se encuentra en una sección específica (por ejemplo, visualización de imágenes).
Funciones Principales
handle_navigation_bar
Maneja la barra de navegación en la interfaz.

display_images
Muestra las imágenes originales y transformadas en la pantalla.

transform_image
Carga una imagen, la convierte en un array NumPy y llama a la función de transformación correspondiente.

display_default_images
Muestra la sección de imágenes predeterminadas para un animal específico.

display_upload_image
Permite al usuario cargar una imagen y muestra la sección correspondiente.

display_webcam
Activa la cámara web para simular la visión de un animal.

handle_mouse_click
Maneja los clics del mouse en la interfaz.

cleanup_resources
Libera recursos como la cámara web y destruye ventanas abiertas.

display_menu
Muestra el menú principal en la interfaz.

main
La función principal que inicia el programa, maneja eventos y llama a funciones según la entrada del usuario.

mainCode.py
Funciones de Transformación
transform_to_dog_sight
Simula la visión dicromática eliminando el canal rojo de la imagen.

transform_to_bee_sight
Simula la visión ultravioleta ajustando los canales de color.

transform_to_bat_sight
Simula la ecolocación aplicando un filtro Laplaciano.

transform_to_snake_sight
Simula la visión infrarroja ajustando los canales de color.

## Uso
El programa se inicia desde mainGUI.py. Se presenta un menú principal donde el usuario puede seleccionar entre visualizaciones predeterminadas, cargar una imagen o utilizar la cámara web. La aplicación simula la visión de diferentes animales según la elección del usuario.

## Conclusión
"Animal Sight" proporciona una experiencia interactiva para explorar y comprender cómo los diferentes animales ven el mundo. La combinación de Pygame, OpenCV y NumPy permite una representación visual impactante de las diferentes perspectivas animales.
