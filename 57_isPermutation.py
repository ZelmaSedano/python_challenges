def is_permutation(str1, str2):
    # edgecase: if str1 AND str2 are empty
    if not str1 or str1.isspace() and not str2 or str2.isspace():
        return 'please add letters to both strings'
    # edgecase: if str1 or str2 are empty
    if not str1 or str1.isspace():
        return 'please add letters to string #1'
    elif not str2 or str2.isspace():
        return 'please add letters to string #2'

    # if the str2 is a permutation os str1, then they will be the same if you sort their letters
    return sorted(str1) == sorted(str2)

print(is_permutation('', ''))
