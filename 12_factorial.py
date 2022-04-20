def factorial(num):
    # edgecase: if num is negative - factorials of negative numbers are considered 'complex numbers'
    if num < 0:
        return 'the factorial is a complex number'

    # if num is 0, return 1 b/c that's the factorial of 0
    if num == 0:
        return 1

    # create a variable to hold result and multiply by
    result = 1

    # loop from 1 to num in a range (not 0 b/c we're multiplying)
    # remember, a range creates a list of iterable integers 
    for i in range(1, num + 1):
        result *= i

    return result

print(factorial(5))
