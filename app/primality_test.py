import math

def primality_test(number):
    try:
        number = int(number)
    except ValueError:
        return "Wrong data"
    
    if number <= 1 or number > 9223372036854775807:
        return "Wrong data"

    for i in (range(2, int(math.sqrt(number))+1)):
        if number % i == 0:
            return f"{number} is not a prime number"
    return f"{number} is a prime number"