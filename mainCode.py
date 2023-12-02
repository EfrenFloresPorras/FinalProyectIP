# mainCode.py

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

    return cv.cvtColor(final_img, cv.COLOR_BGR2RGB)

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

    return cv.cvtColor(uv_image, cv.COLOR_BGR2RGB)

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

def transform_to_snake_sight(img_link):
    # Infrared vision
    img = cv.imread(img_link)

    # Split channels
    b, g, r = cv.split(img)

    # Convert channels to NumPy arrays
    b = np.array(b, dtype=np.float32)
    g = np.array(g, dtype=np.float32)
    r = np.array(r, dtype=np.float32)
    
    infrared_img = img.copy()
    infrared_img[:, :, 0] = b * 0.5
    infrared_img[:, :, 1] = g * 1.5
    infrared_img[:, :, 2] = r * 3

    return cv.cvtColor(infrared_img, cv.COLOR_BGR2RGB)
