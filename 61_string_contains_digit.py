def contains_digits(str):
    # loop through str
    for i in str:
        if i.isdigit():
            return True

    # backup
    return False

print(contains_digits('hi3'))
