def removeSpaces(str):
    # edge case: if str is empty, return message
    if len(str) == 0:
        return 'please add some words to your string'
    elif str.isspace():
        return 'please add some words to your string'
    return str.replace(' ', '')

print(removeSpaces(' '))
