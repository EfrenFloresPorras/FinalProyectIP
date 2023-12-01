# mainGUI.py

import pygame
import sys
from tkinter import Tk, filedialog
import cv2
import numpy as np
from mainCode import *
# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animal Sight Visualization")

# Font settings
font = pygame.font.Font(None, 36)
selected_font = pygame.font.Font(None, 40)

# Variables
animal_sight_type = "Dog"
animals = ["Dog", "Bee", "Bat", "Snake"]
menu_active = True
menu_option = None

# Open file dialog to get image path
root = Tk()
root.withdraw()


# Function to handle navigation bar
def handle_navigation_bar(animals, menu_active):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            return handle_mouse_click(event.pos, animals, menu_active, None, False)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0 or event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                return int(event.key)
    return None


# Function to display the images
def display_images(original_image, transformed_image):
    # Display original image
    screen.blit(original_image, (50, 50))

    # Display transformed image
    screen.blit(transformed_image, (550, 50))

    # Display return to menu button
    text_return = font.render("Return to Menu", True, BLACK)
    pygame.draw.rect(screen, WHITE, (600, 500, 150, 40))
    screen.blit(text_return, (600, 500))

    pygame.display.flip()


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


# Function to display the default images section
def display_default_images(section_active):
    # Initialize the flag
    section_active = True
    animal_sight_type = "Dog"

    while section_active:
        screen.fill(WHITE)
        
        # Display navigation bar
        for i, animal in enumerate(animals):
            text_animal = selected_font.render(animal, True, BLACK) if animal == animal_sight_type else font.render(animal, True, BLACK)
            screen.blit(text_animal, (i * (screen_width // len(animals)), 0))

        # Display the images
        original_image, transformed_image = transform_image(f"images/{animal_sight_type.lower()}.jpg", animal_sight_type)
        display_images(original_image, transformed_image)

        # Display return to menu button
        text_return = font.render("Return to Menu", True, BLACK)
        pygame.draw.rect(screen, WHITE, (600, 500, 150, 40))
        screen.blit(text_return, (600, 500))

        pygame.display.flip()

        # Event handling within the loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                section_active = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 600 <= event.pos[0] <= 750 and 500 <= event.pos[1] <= 540:
                    print("Return to Menu button clicked")
                    section_active = False
                else:
                    for i, animal in enumerate(animals):
                        x = i * (screen_width // len(animals))
                        if x <= event.pos[0] <= x + screen_width // len(animals) and 0 <= event.pos[1] <= 40:
                            animal_sight_type = animal
                            print(f"Animal selected: {animal}")
                            # Keep the section active to continue displaying images
                            # Let's print a message indicating that the images should change
                            print("Images should change for the selected animal")

    # Reset the flag to stay in the section
    section_active = False

    # Return to the main menu
    return True, animal_sight_type, None, False


# Function to display the upload image section
def display_upload_image(section_active):
    # Initialize the flag
    section_active = True
    animal_sight_type = "Dog"

    # Open file dialog to get image path
    image_path = filedialog.askopenfilename()

    while section_active:
        screen.fill(WHITE)

        # Check if an image was selected
        if not image_path:
            return True, animal_sight_type, None, False  # No image selected, return to the menu

        if image_path:
            original_image, transformed_image = transform_image(image_path, animal_sight_type)
            display_images(original_image, transformed_image)

            # Display navigation bar
            for i, animal in enumerate(animals):
                text_animal = selected_font.render(animal, True, BLACK) if animal == animal_sight_type else font.render(animal, True, BLACK)
                screen.blit(text_animal, (i * (screen_width // len(animals)), 0))

            # Display return to menu button
            text_return = font.render("Return to Menu", True, BLACK)
            pygame.draw.rect(screen, WHITE, (600, 500, 150, 40))
            screen.blit(text_return, (600, 500))

            pygame.display.flip()

            # Event handling within the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    section_active = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 600 <= event.pos[0] <= 750 and 500 <= event.pos[1] <= 540:
                        print("Return to Menu button clicked")
                        section_active = False
                    else:
                        for i, animal in enumerate(animals):
                            x = i * (screen_width // len(animals))
                            if x <= event.pos[0] <= x + screen_width // len(animals) and 0 <= event.pos[1] <= 40:
                                animal_sight_type = animal
                                print(f"Animal selected: {animal}")
                                # Keep the section active to continue displaying images
                                # Let's print a message indicating that the images should change
                                print("Images should change for the selected animal")

    # Reset the flag to stay in the section
    section_active = False

    # Return to the main menu
    return True, animal_sight_type, None, False


# Function to display the webcam section
def display_webcam(section_active):
    # Initialize the flag
    section_active = True
    animal_sight_type = "Dog"

    while section_active:
        screen.fill(WHITE)
        cap = cv2.VideoCapture(0)

        # Display navigation bar
        for i, animal in enumerate(animals):
            text_animal = selected_font.render(animal, True, BLACK) if animal == animal_sight_type else font.render(animal, True, BLACK)
            screen.blit(text_animal, (i * (screen_width // len(animals)), 0))

        pygame.display.flip()

        # Create surfaces for left and right sections
        left_section = pygame.Surface((350, 350))
        right_section = pygame.Surface((350, 350))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cap.release()
                    cv2.destroyAllWindows()
                    pygame.quit()
                    sys.exit()

                _, frame = cap.read()

                # Resize the frame to match surface dimensions
                frame = cv2.resize(frame, (350, 350))

                # Debug statement: Display the selected animal before and after transformation
                print(f"Before transformation: {animal_sight_type}")
                
                # Add transformation to the webcam frame according to the selected animal
                if animal_sight_type == "Dog":
                    transformed_frame = transform_to_dog_sight(frame)
                elif animal_sight_type == "Bee":
                    transformed_frame = transform_to_bee_sight(frame)
                elif animal_sight_type == "Bat":
                    transformed_frame = transform_to_bat_sight(frame)
                    transformed_frame = transformed_frame.astype(np.uint8)
                elif animal_sight_type == "Snake":
                    transformed_frame = transform_to_snake_sight(frame)
                else:
                    transformed_frame = frame

                print(f"After transformation: {animal_sight_type}")

                # Display the original frame on the left
                if isinstance(frame, np.ndarray) and frame.size > 0:  # Check if the object is a NumPy array and non-empty
                    pygame.surfarray.blit_array(left_section, np.swapaxes(frame, 0, 1))

                # Display the transformed frame on the right
                if isinstance(transformed_frame, np.ndarray) and transformed_frame.size > 0:  # Check if the object is a NumPy array and non-empty
                    pygame.surfarray.blit_array(right_section, np.swapaxes(transformed_frame, 0, 1))

                # Blit the left and right sections onto the main screen
                screen.blit(left_section, (50, 50))
                screen.blit(right_section, (500, 50))

                pygame.display.flip()

                # Break the loop if 'q' key is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                # Break the loop if a different animal_sight_type is selected
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    selected_index = x // (screen_width // len(animals))
                    animal_sight_type = animals[selected_index]
                    break

        cap.release()
        cv2.destroyAllWindows()

    # Reset the flag to stay in the section
    section_active = False

    # Return to the main menu
    return True, animal_sight_type, None, False



# Flag to track whether to display the main menu
menu_active = True

# Flag to track whether to stay in the current section
section_active = False


# Function to handle mouse clicks
def handle_mouse_click(position, animals, menu_active, menu_option, section_active):
    global animal_sight_type  # Declare as global variable

    if not menu_active:
        # If not in the menu, check for the "Return to Menu" button
        if 600 <= position[0] <= 750 and 500 <= position[1] <= 540:
            print("Return to Menu button clicked")
            return True, animal_sight_type, None, False  # Set back to False when returning to the menu

        for i, animal in enumerate(animals):
            x = i * (screen_width // len(animals))
            if x <= position[0] <= x + screen_width // len(animals) and 0 <= position[1] <= 40:
                animal_sight_type = animal
                print(f"Animal selected: {animal}")
                return menu_active, animal_sight_type, menu_option, False  # Set back to False when an animal is selected
    else:
        # If in the menu, check for other options
        menu_options = ["Default Images", "Upload Image", "Webcam Image", "Exit"]
        for i, option in enumerate(menu_options):
            option_rect = pygame.Rect(50, 200 + i * 100, font.size(option)[0], font.size(option)[1])
            print(f"Option: {option}, Coordinates: {option_rect}")
            if option_rect.collidepoint(*position):
                if option == "Default Images":
                    print("Default Images selected")
                    display_default_images(section_active)
                    return False, animal_sight_type, "1", True  # Set to True when entering a section
                elif option == "Upload Image":
                    print("Upload Image selected")
                    display_upload_image(section_active)
                    return False, animal_sight_type, "2", True  # Set to True when entering a section
                elif option == "Webcam Image":
                    print("Webcam Image selected")
                    display_webcam(section_active)
                    return False, animal_sight_type, "3", True  # Set to True when entering a section
                elif option == "Exit":
                    print("Exit selected")
                    pygame.quit()
                    cleanup_resources()
                    sys.exit()

    return menu_active, animal_sight_type, menu_option, section_active


# Function to cleanup resources
def cleanup_resources(cap=None):
    if cap is not None:
        cap.release()  
    cv2.destroyAllWindows()


# Function to display the main menus
def display_menu(menu_option=None):
    screen.fill(WHITE)
    text_welcome = font.render("MENÚ", True, BLACK)
    screen.blit(text_welcome, (screen_width // 2 - text_welcome.get_width() // 2, 150))
    pygame.display.flip()

    menu_options = ["1. Default Images", "2. Upload Image", "3. Webcam Image", "0. Exit"]

    for i, option in enumerate(menu_options):
        if menu_option == option:
            option_text = selected_font.render(option, True, BLACK)
        else:
            option_text = font.render(option, True, BLACK)

        screen.blit(option_text, (50, 200 + i * 100))

    pygame.display.flip()

# ...

def main():
    # Display welcome message
    screen.fill(WHITE)
    text_welcome = font.render("Welcome to the Animal Sight Visualization Program!", True, BLACK)
    text_welcome2 = font.render("Press any key to continue...", True, BLACK)
    screen.blit(text_welcome, (50, 50))
    screen.blit(text_welcome2, (50, 100))
    pygame.display.flip()

    # Wait for a key press to continue
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                waiting_for_key = False  # Set waiting_for_key to False when a key is pressed
                break  # Break out of the loop when a key is pressed

    # Main loop
    menu_option = None  # Added variable to keep track of the selected menu option
    current_display = None  # Added variable to keep track of the current display
    menu_active = True  # Set menu_active to True initially
    section_active = False  # Set section_active to False initially
    current_display = None  # Initialize current_display outside the loop

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cleanup_resources()
                pygame.quit()
                sys.exit()

            # Handling key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key == pygame.K_ESCAPE:
                    cleanup_resources()
                    pygame.quit()
                    sys.exit()
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    animal_sight_type = None  # Assign a default value to animal_sight_type
                    if event.key == pygame.K_1:
                        current_display = display_default_images
                    elif event.key == pygame.K_2:
                        current_display = display_upload_image
                    elif event.key == pygame.K_3:
                        current_display = display_webcam

            # Handling mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                menu_active, animal_sight_type, menu_option, section_active = handle_mouse_click(event.pos, animals, menu_active, menu_option, section_active)

        # If there's a current display, execute it
        if current_display is not None:
            menu_active, animal_sight_type, menu_option, section_active = current_display(section_active)
            current_display = None  # Reset current_display after executing

            if menu_option is not None:
                display_menu(menu_option)

        else:
            menu_option = None
            section_active = False
            display_menu(menu_option)

        pygame.display.flip()
        pygame.time.delay(30)

if __name__ == "__main__":
    main()