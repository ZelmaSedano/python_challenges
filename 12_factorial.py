def factorial(num):
    # edgecase: if num is negative b/c negative factorials are considered complex numbers
    if num < 0:
        return 'please only use positive numbers b/c negative factorials are complex numbers'
    # if num is 0, return 1 b/c the factorial of 0 is 1 
    if num == 0:
        return 1

    # create a result variable & set it to 1 b/c we're multiplying by it
    result = 1

    # loop from 1 to num, including num
    for i in range(1, num+1):
        result *= i

    return result
    
print(factorial(5))
