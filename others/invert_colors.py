from PIL import Image, ImageChops

def invert_colors(filename):
    img = Image.open(filename)
    result = ImageChops.invert(img)
    return result