def find_divisors(num=None):
    if num == None:
        return 'please enter a number'

   # create an empty divisors array
    divisors = []

    # loop from 2 to int, 1 will always divide into int_
    # don't add +1 after int_, since the num will always be divisible by itself, even when prime
    for i in range(2, int_):
        if int_ % i == 0:
            divisors.append(i)

    # if there aren't any divisors, it's a prime
    if len(divisors) == 0:
        return 'number is a prime'
    else:
        return divisors
    
print(find_divisors(18))
