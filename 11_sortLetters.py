def sort_letters(str):
    if not str:
        return 'please add letters to string'

    # remove the spaces
    str = str.replace(' ', '')
    # sort the letters, then join outside & return
    return ''.join(sorted(str))

print(sort_letters(''))
