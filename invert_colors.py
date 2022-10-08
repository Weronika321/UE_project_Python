from PIL import Image, ImageChops

def inwersja_kolorow(obrazek):
    obrazek_inw = ImageChops.invert(obrazek)
    obrazek_inw.show()
    

#obrazek = Image.open("obrazek.jpg")
#inwersja_kolorow(obrazek)