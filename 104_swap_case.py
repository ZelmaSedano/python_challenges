# there's a built-in .swapcase() method you can use
def swap_case(string):
    return string.swapcase()

print(swap_case('Hi'))


# or you can do it the long way
def swap_case(string):
    result = []

    for c in string:
        if c.isupper():
            result.append(c.lower())
        elif c.islower():
            result.append(c.upper())
        else:
            result.append(c)

    return ''.join(result)

print(swap_case('Hi'))
