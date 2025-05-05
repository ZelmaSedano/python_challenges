def longest_word(string):
    # remove all trailing and between spaces
    words = string.split()

    # create an empty variable to hold longest word
    longest = ''

    # loop through the list of words
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

print(longest_word('hi there'))
