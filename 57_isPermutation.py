def isPermutation(str1, str2):
    return sorted(str1) == sorted(str2)

print(isPermutation('howdy', 'dwhoy'))
