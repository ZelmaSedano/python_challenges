def is_integer(num):
    # edgecase: don't enter decimals
    if isinstance(num, float):
        return 'please only use whole numbers'

    return type(num) == int

print(is_integer(-17))
