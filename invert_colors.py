from PIL import Image, ImageChops

def invert_colors(filename):
    obrazek = Image.open(filename)
    obrazek_inw = ImageChops.invert(obrazek)
    return obrazek_inw
    # obrazek_inw.show()
    

#obrazek = Image.open("obrazek.jpg")
#inwersja_kolorow(obrazek)