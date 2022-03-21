def square_digits(num):
    # edgecase: if num is negative, can't square
    if num < 0:
        return 'please only use positive numbers'

    # create a variable that you can return
    result = []

    # cast num into a string and split it into a list
    arr = list(str(num))

    # loop through the list
    for i in arr:
        # make a variable to be integer version of i
        y = int(i)

        # append and cast to string the squared digit
        result.append(str(y*y))

    # create a newString that is the joined result list
    newStr = ''.join(result)

    return int(newStr)

print(square_digits(13))
