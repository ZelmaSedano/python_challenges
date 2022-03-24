# this is a little different from removing all duplicates b/c we want to keep single-occurring items
# if we used set, it would remove the single-occurring items 
def remove_doubles(str):
    # edgecase: is string is empty
    if not str or str.isspace():
        return 'please add letters to string'

    # create an empty string to return
    result = ''

    # loop through string
    for i in range(len(str)):
        # make sure the char isn't the last char, otherwise it'll try and look for the next element
        if i != len(str)-1:
            # if the current char and the next char are the same, append one to result
            if str[i] == str[i+1]:
                result += str[i]
        # if char IS the last character
        if i == len(str)-1:
            # make sure that you're not adding a double by making sure the char b/f isn't the same 
            if str[i] != str[i-1]:
                result += str[i]

    return result

print(remove_doubles('aabbddeeaa'))
