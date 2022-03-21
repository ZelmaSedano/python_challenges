def is_str_unique(str):
    # edgecase: if string is empty
    if not str or str.isspace():
        return 'please add letters to string'

    # remove all the duplicates from the string using set and compare it to str
    # when you use set in python, it doesn't keep the original order of the letters, so order them
    return sorted(set(str)) == sorted(str)

print(is_str_unique('helo'))
