def square_digits(num):
    result = []

    words = list(str(num))

    for i in words:
        y = int(i)
        result.append(str(y*y))

    newStr = ''.join(result)
    return int(newStr)


print(square_digits(13))
