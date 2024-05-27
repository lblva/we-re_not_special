import os
import cv2
import mediapipe as mp
import numpy as np
import time 
import random
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load your audio file
audio_file = "public/glittergeluid.mp3"
pygame.mixer.music.load(audio_file)

mp_selfie_segmentation = mp.solutions.selfie_segmentation

BG_COLOR = (192, 192, 192)  # Gray
FADE_DURATION = 10 * 60  # Fade duration in seconds
FADE_STEPS = 50  # Number of steps for fading

# Function to generate a random pastel color with emphasis on blue, green, yellow, and orange
def generate_pastel_color():
    return (
        random.randint(100, 255),  # R component (emphasis on blue and red)
        random.randint(100, 255),    # G component (emphasis on green and yellow)
        random.randint(100, 255)    # B component (emphasis on blue and green)
    )

# Assign pastel colors to detected persons
person_colors = {}

# Fade out function
def fade_out(image):
    alpha_step = 1.0 / FADE_STEPS
    for i in range(FADE_STEPS):
        alpha = 1.0 - alpha_step * i
        overlay = image.copy()
        cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
        cv2.imshow("MediaPipe Selfie Segmentation", image)
        cv2.waitKey(int(FADE_DURATION * 300 / (FADE_STEPS * FADE_STEPS)))  # Delay between each step

# Specify the path to your public folder
public_folder_path = "public"

cap = cv2.VideoCapture(0)
audio_playing = False  # Flag to track if audio is already playing


with mp_selfie_segmentation.SelfieSegmentation(model_selection=0) as selfie_segmentation:
    bg_image = None

    # Initialize variables for tracking stillness
    start_still_time = None
    is_still = False

    # Initialize variables for capturing the image
    capture_start_time = None
    captured = False
    captured_image = None

    # Counter to keep track of the number of images saved
    image_counter = 1

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue  # Skip the rest of the loop if frame read was unsuccessful

        start = time.time()
        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        # To improve performance, optionally mark the image as not writable to
        # pass by reference.
        image.flags.writeable = False

        # Pass the image through the model
        results = selfie_segmentation.process(image)
        cv2.imshow('Segmentation Mask', results.segmentation_mask)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Create blank canvas filled with background color
        bg_canvas = np.full(image.shape, BG_COLOR, dtype=np.uint8)

        # Get the contours of the segmentation mask
        contours, _ = cv2.findContours((results.segmentation_mask > 0.15).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filter out contours with areas smaller than a threshold
        valid_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]

        # Assign pastel colors to detected persons
        if len(valid_contours) > 0:
            # Reset colors when a person is detected
            person_colors = {}
            # Play audio only if it's not already playing
            if not audio_playing:
                pygame.mixer.music.play()
                audio_playing = True

        for i, cnt in enumerate(valid_contours):
            if i not in person_colors:
                # Generate a random pastel color for each contour
                color = generate_pastel_color()
                person_colors[i] = color
            mask = np.zeros_like(results.segmentation_mask)
            cv2.drawContours(mask, [cnt], -1, (255), thickness=cv2.FILLED)
            bg_canvas[mask == 255] = person_colors[i]

        # Update the number of persons detected
        num_persons = len(valid_contours)

        # Combine the background canvas with the original image
        output_image = np.where(bg_canvas == BG_COLOR, image, bg_canvas)

        end = time.time()
        totalTime = end - start

        if totalTime != 0:
            fps = 1 / totalTime
            print("FPS: ", fps)
        else:
            print("Total time is zero, FPS calculation skipped.")
            
        # Check if the person is staying still
        if not captured and not is_still:
            if start_still_time is None:
                start_still_time = time.time()
            elif time.time() - start_still_time >= 3:  # 3 seconds
                # Capture image when person stays still for 3 seconds
                captured = True
                capture_start_time = time.time()
                captured_image = output_image.copy()
                # Save the colored silhouette mask with transparency
                colored_silhouette_mask_alpha = np.zeros((*output_image.shape[:2], 4), dtype=np.uint8)
                for i, cnt in enumerate(valid_contours):
                    mask = np.zeros_like(results.segmentation_mask)
                    cv2.drawContours(mask, [cnt], -1, (255), thickness=cv2.FILLED)
                    colored_silhouette_mask_alpha[mask == 255] = (*person_colors[i], 255)  # Set alpha to 255 for silhouette regions

                # Save the image with transparency to the public folder
                image_name = f"silhouette_{image_counter}.png"
                destination_path = os.path.join(public_folder_path, image_name)
                cv2.imwrite(destination_path, colored_silhouette_mask_alpha)

                image_counter += 1
                if image_counter > 20:
                    image_counter = 1

 
        elif captured and time.time() - capture_start_time >= 3:  
            fade_out(captured_image)  # Fade out the captured image
            print("Captured image faded out.")
            captured = False
            start_still_time = None  # Restart the stillness timer
            is_still = False  # Reset the stillness flag

            # Stop audio after displaying the captured image
            pygame.mixer.music.stop()
            audio_playing = False

        if captured:
            cv2.imshow('MediaPipe Selfie Segmentation', captured_image)
        else:
            cv2.imshow('MediaPipe Selfie Segmentation', output_image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
