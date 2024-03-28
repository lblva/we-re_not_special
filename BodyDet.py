import cv2
import mediapipe as mp
import numpy as np
import time 

mp_selfie_segmentation = mp.solutions.selfie_segmentation

BG_COLOR = (192, 192, 192)  # Gray
FADE_DURATION = 10 * 60  # Fade duration in seconds
FADE_STEPS = 50  # Number of steps for fading

person_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Blue, Green, Red

def fade_out(image):
    alpha_step = 1.0 / FADE_STEPS
    for i in range(FADE_STEPS):
        alpha = 1.0 - alpha_step * i
        overlay = image.copy()
        cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)
        cv2.imshow("MediaPipe Selfie Segmentation", image)
        cv2.waitKey(int(FADE_DURATION * 300 / (FADE_STEPS * FADE_STEPS)))  # Delay between each step

cap = cv2.VideoCapture(0)

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

        # Assign colors to detected persons
        for i, cnt in enumerate(valid_contours):
            mask = np.zeros_like(results.segmentation_mask)
            cv2.drawContours(mask, [cnt], -1, (255), thickness=cv2.FILLED)
            bg_canvas[mask == 255] = person_colors[i % len(person_colors)]

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
                    colored_silhouette_mask_alpha[mask == 255] = (*person_colors[i % len(person_colors)], 255)  # Set alpha to 255 for silhouette regions

                # Save the image with transparency
                cv2.imwrite(f"silhouette_{image_counter}.png", colored_silhouette_mask_alpha)

                image_counter += 1
                if image_counter > 20:
                    image_counter = 1

 
        elif captured and time.time() - capture_start_time >= 3:  # Display for 20 seconds
            fade_out(captured_image)  # Fade out the captured image
            print("Captured image faded out.")
            captured = False
            start_still_time = None  # Restart the stillness timer
            is_still = False  # Reset the stillness flag

        if captured:
            cv2.imshow('MediaPipe Selfie Segmentation', captured_image)
        else:
            cv2.imshow('MediaPipe Selfie Segmentation', output_image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()