import math

def is_prime(liczba):
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