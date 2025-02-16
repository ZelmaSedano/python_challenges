def longest_word(str):
    # create a longest word variable
    longest = ''

    # split the string into words
    words = str.split(' ')

    # loop through the words list
    # since it's a list of words, you don't need to make a range b/c i = word
    for i in words:
        if len(i) > len(longest):
            longest = i

    return longest

print(longest_word('hi there'))
