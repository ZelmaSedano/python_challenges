def truncate_string(str, target):
    # edgecase: if string is empty
    if not str or str.isspace():
        return 'please add letters to string'
    
    # use slicing to slice off the string at a certain target
    return str[0:target]

print(truncate_string('hello', 3))
