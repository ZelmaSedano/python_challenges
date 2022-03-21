def is_string_unique(str):
    # edgecase: if string is empty
    if not str:
        return 'please add letters to string'

    # when you create a set in python, it doesn't keep the original order of the elements when it's a string
    # so you have to sort them
    return sorted(set(str)) == sorted(str)

print(is_string_unique('hi'))
