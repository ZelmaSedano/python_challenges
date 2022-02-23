def squareDigits(num):
    return ''.join(str(int(i)**2) for i in str(num))


print(squareDigits(123))
