def square_digits(num):
    # edgecase: if num is negative
    if num < 0:
        return 'please only use positive numbers'

    # create a result variable to return
    result = []

    # create a string version of num and split it 
    arr = list(str(num))

    # loop through list
    for i in arr:
        # create an int version of i
        y = int(i)

        # square y and append to result
        result.append(str(y*y))

    # join the list and convert to int
    return int(''.join(result))

print(square_digits(29))
