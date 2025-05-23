def num_is_squared(num):
    # num ** 0.5 calculates the square root of a number
    # int() converts the square root to an integer
    # **2 squares the integer obtained from prev step
    # == num, checks to see if num is the same as the result, therefore it's a square
    return int(num ** 0.5) ** 2 == num

print(num_is_squared(16))
