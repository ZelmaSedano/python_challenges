def square_digits(num):
    # edgecase: if num is negative
    if num < 0:
        return 'please only use positive numbers'

    # create a result variable to return
    result = []

    # cast the num into a string, and split it
    arr = list(str(num))

    # loop through the list
    for i in arr:
        # create a variable to hold the number version of i 
        y = int(i)

        # square the number and add it to result list as string
        result.append(str(y*y))

    # create a new string with the joined result
    newStr = ''.join(result)

    # return the string converted to an integer
    return int(newStr)

print(square_digits(13))
