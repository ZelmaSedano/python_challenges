def is_permutation(str1, str2):
    # edgecase: if both strings are empty
    if not str1 and not str2:
        return 'please add letters to both strings'
    # edgecase: if str1 is empty
    if not str1 or str1.isspace():
        return 'please add letters to str1'
    # edgecase: if str2 is empty
    elif not str2 or str2.isspace():
        return 'please add letters to str2'

    # if they are permutations of each other, then if each word is sorted they should equal each other
    return sorted(str1) == sorted(str2)

print(is_permutation('', 'd'))
