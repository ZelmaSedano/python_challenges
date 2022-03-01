def longestWord(str):
    if not str:
        return 'please add words to string'
    # create empty longest variable
    longest = ''
    # split the str into list of words
    list = str.split(' ')

    for i in list:
        if len(i) > len(longest):
            longest = i

    return longest

print(longestWord(''))
