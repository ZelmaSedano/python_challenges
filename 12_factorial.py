def factorial(num):
    # edgecases: negative numbers don't have a factorial
    if num < 0:
        return 'negative numbers do not have a factorial'

    # if num is 0, factorial is 1
    if num == 0:
        return 1

    # create a result variable to hold result & set it to 1 b/c we're multiplying by it
    result = 1

    # loop from 1 to num, including num
    for i in range(1, num+1):
        result *= i

    return result

print(factorial(5))
