def is_integer(num):
    # you don't need an edgecase, because anything that's NOT an integer will return false
    return type(num) == int

print(is_integer(15.5))
