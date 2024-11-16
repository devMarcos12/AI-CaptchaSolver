import os
from PIL import Image
import cv2
import numpy as np

# Input and output folder paths
input_folder = "./data/raw/"
processed_folder = "./data/processed/"
denoised_folder = "./data/denoised/"

# Create necessary folders
os.makedirs(processed_folder, exist_ok=True)
os.makedirs(denoised_folder, exist_ok=True)

# Process each image in the input folder
for image_name in os.listdir(input_folder):
    if image_name.endswith(".png"):
        # Open the raw image
        image_path = os.path.join(input_folder, image_name)
        image = Image.open(image_path)

        # Convert the image to grey scale
        grayscale_image = image.convert("L")
        processed_path = os.path.join(processed_folder, image_name)
        grayscale_image.save(processed_path)
        print(f"Grayscale: {image_name}")

        # Remove noise using thresholding
        grayscale_image_cv2 = cv2.imread(processed_path, cv2.IMREAD_GRAYSCALE)
        # Apply Gaussian blur to reduce noise before thresholding
        image_blur = cv2.GaussianBlur(grayscale_image_cv2, (3, 3), 0)

        # Apply thresholding
        _, denoised_image = cv2.threshold(image_blur, 170, 255, cv2.THRESH_BINARY)

        # Remove small noise based on contour area
        contours, _ = cv2.findContours(denoised_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) < 50:  # Adjust the area threshold as needed
                cv2.drawContours(denoised_image, [contour], -1, (0, 0, 0), -1)

        # Apply median blur to smooth edges
        denoised_image = cv2.medianBlur(denoised_image, 3)

        # Save the refined image
        denoised_path = os.path.join(denoised_folder, image_name)
        cv2.imwrite(denoised_path, denoised_image)
        print(f"Refined: {image_name}")





