# mainCode.py

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pygame

# Function to transform an image
def transform_image(image_path, animal_sight_type):
    original_image = pygame.image.load(image_path)
    original_image = pygame.transform.scale(original_image, (400, 400))

    # Convert the image to a NumPy array
    original_array = pygame.surfarray.array3d(original_image)

    if animal_sight_type == "Dog":
        transformed_image = pygame.surfarray.make_surface(np.swapaxes(transform_to_dog_sight(original_array), 0, 1))
    elif animal_sight_type == "Bee":
        transformed_image = pygame.surfarray.make_surface(np.swapaxes(transform_to_bee_sight(original_array), 0, 1))
    elif animal_sight_type == "Bat":
        transformed_image = pygame.surfarray.make_surface(np.swapaxes(transform_to_bat_sight(original_array), 0, 1))
    elif animal_sight_type == "Snake":
        transformed_image = pygame.surfarray.make_surface(np.swapaxes(transform_to_snake_sight(original_array), 0, 1))
    else:
        transformed_image = pygame.surfarray.make_surface(np.swapaxes(original_array, 0, 1))

    return original_image, transformed_image

def transform_to_dog_sight(image):
    # Dicromatic vision
    img = cv.imread(image)[:, :, :: -1]

    # Delete red channel
    delete_red = img.copy()
    delete_red[:, :, 2] = 0

    # Merge blue and green channels
    final_img = delete_red[:, :, [1, 0, 0]]

    return final_img

def transform_to_bee_sight(image):
    # Ultra violet vision
    img = cv.imread(image)

    # Split channels
    b, g, r = cv.split(img)

    # Convert channels to NumPy arrays
    b = np.array(b, dtype=np.float32)
    g = np.array(g, dtype=np.float32)
    r = np.array(r, dtype=np.float32)

    # Apply modifications to simulate fluorescence
    uv_image = img.copy()
    uv_image[:, :, 0] = b * 0.5  # Adjusting the blue channel
    uv_image[:, :, 1] = g * 0.5  # Adjusting the green channel
    uv_image[:, :, 2] = r * 1.5  # Adjusting the red channel

    final_img = cv.cvtColor(uv_image, cv.COLOR_BGR2RGB)
    return final_img

def transform_to_bat_sight(image):
    # Eco location
    img_gris = cv.imread(image, 0)
    laplce1 = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
    ])
    final_img = cv.filter2D(img_gris, -1, laplce1)
    return final_img

def transform_to_snake_sight(image):
    # Replace this with actual transformation logic for snake sight
    # For now, just return the original image
    return image

def transform_webcam_image(frame, image):
    # Replace this with actual transformation logic for webcam image
    # For now, just return the original image
    return image


