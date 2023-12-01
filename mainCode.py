# mainCode.py

from typing import final
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pygame

def transform_to_dog_sight(image):
    # Dicromatic vision
    # Delete red channel
    delete_red = image.copy()
    delete_red[:, :, 2] = 0

    # Merge blue and green channels
    final_img = delete_red[:, :, [1, 0, 0]]

    return final_img

def transform_to_bee_sight(image):
    # Ultra violet vision
    # Split channels
    b, g, r = cv.split(image)

    # Convert channels to NumPy arrays
    b = np.array(b, dtype=np.float32)
    g = np.array(g, dtype=np.float32)
    r = np.array(r, dtype=np.float32)

    # Apply modifications to simulate fluorescence
    uv_image = image.copy()
    uv_image[:, :, 0] = b * 0.5  # Adjusting the blue channel
    uv_image[:, :, 1] = g * 0.5  # Adjusting the green channel
    uv_image[:, :, 2] = r * 1.5  # Adjusting the red channel

    final_img = cv.cvtColor(uv_image, cv.COLOR_BGR2RGB)
    return final_img

def transform_to_bat_sight(image):
    # Eco location
    img_gris = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
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