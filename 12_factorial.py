def factorial(num=None):
    if num is None:
        return 'please add number to argument'

    # create a result variable & set it to 1 since we'll be multiplying using it
    result = 1

    # edgecase: if num is under 0, return message
    if num < 0:
        return 'Sorry, factorial does not exist this number'
    # if num is 0, return message
    elif num == 0:
        return 'The factorial of 0 is 1'
    else:
        # loop from 1 to num, including num
        for i in range(1, num+1):
            result *= i
    
    # return the factorial
    return result

print('the factorial is:')
print(factorial(5))
