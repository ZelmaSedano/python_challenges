def is_string_unique(str):
    # edgecase: if string is empty
    if not str or str.isspace():
        return 'please add letters to string'

    # check to see if string equals set of string
    # set can change the order of the characters, so you have to sort both string and set to check them against each other
    return sorted(set(str)) == sorted(str)


print(is_string_unique('hoo'))
