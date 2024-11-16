import random
import string
from captcha.image import ImageCaptcha

# Configuration: Set the folder to save generated captchas
output_folder = "./data/raw/"  # Path where images will be saved
image_generator = ImageCaptcha()  # Initialize the captcha image generator

# Number of captchas to generate
n_captchas = 10  # Start with 10 for testing, then increase as needed

for i in range(n_captchas):
    # Generate a random string (6 characters: letters and digits)
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Generate the captcha image based on the text
    image = image_generator.generate_image(captcha_text)

    # Save the image to the specified folder
    image.save(f"{output_folder}{captcha_text}.png")
    print(f"Generated: {captcha_text}.png")  # Output the name of the generated captcha
