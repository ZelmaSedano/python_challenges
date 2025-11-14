# check if a given number is the square of a number
def num_is_squared(num):
    # int(17**0.5) = 4
    # 17**0.5=4 = 4.123s
    # if you remove int, it false returns True
    return int(num**0.5)**2 == num

print(num_is_squared(17))
