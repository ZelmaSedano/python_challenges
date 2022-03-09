def isInt(num=None):
    if num is None:
        return 'please add a number to the 2nd argument'

    return type(num) == int

print(isInt('hi'))
