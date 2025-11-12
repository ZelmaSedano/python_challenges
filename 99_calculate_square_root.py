# import the math library
import math

def square_root(num):
    # return the square root with 3 decimal points
    return round(math.sqrt(num), 3)

print(square_root(18))

#####################################################################################

# easier
def square_root(num):
    return num**0.5

print(square_root(16))
