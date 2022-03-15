def is_permutation(str1, str2):
    # edgecase: if string is empty
    if not str1 or str1.isspace():
        return 'please add letters to first string'
    elif not str2 or str2.isspace():
        return 'please add letters to second string'

    # sort the two strings and compare
    return sorted(str1) == sorted(str2)

print(is_permutation('hello', 'llohe'))
