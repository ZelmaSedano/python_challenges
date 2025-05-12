import math

def calculate_square_root(number):
    if number < 0:
        return None
    return round(math.sqrt(number), 5)

print(calculate_square_root(16))  
