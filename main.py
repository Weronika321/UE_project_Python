import math
from PIL import Image, ImageChops

def czy_pierwsza(liczba):
    try:
        int(liczba)
    except ValueError:
        return False
    liczba = int(liczba)
    if liczba < 2:
        return False
    liczba = int(liczba)
    for i in (range(2, int(math.sqrt(liczba)))):
        if liczba % i == 0:
            return False
    return True


def inwersja_kolorow(obrazek):
    obrazek_inw = ImageChops.invert(obrazek)
    obrazek_inw.show()

def uwierzytelnienie():
    print()



#print("Podaj liczbę: ")
#number = input()
#print(czy_pierwsza(number))

#obrazek = Image.open("obrazek.jpg")
#inwersja_kolorow(obrazek)

