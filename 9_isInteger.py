def is_integer(num):
    # integers can be negative, so no edgecase

    return type(num) == int

print(is_integer('hi'))
