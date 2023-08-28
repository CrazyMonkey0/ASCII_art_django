from PIL import Image

ASCII_CHARS = "@B%8WM#*oahkbdpwmZO0QCJYXzcvnxrjft/\|()1{}[]-_+~<>i!lI;:,"

# Image resizing
def resize(image, new_width=100):
    (width, height) = image.size
    radio = height / width
    new_height = int(radio * new_width * 0.55)
    new_image = image.resize((new_width, new_height))
    return new_image

# Conversion to grayscale
def grayify(image):
    return image.convert("L")

# Mapping pixels to ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    char ="".join([ASCII_CHARS[pixel//10] for pixel in pixels])
    return char

# Creating an ASCII art image
def convert_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except: 
        return "Invalid path"

    new_image_data = pixels_to_ascii(grayify(resize(image)))
    pixel_count = len(new_image_data)
    return "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))