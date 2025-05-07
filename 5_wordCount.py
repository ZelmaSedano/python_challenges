def word_count(string):
    # loop through the split string, (' ') removes spaces
    # if the word isn't a space, add it to words list/array
    # 2. The list comprehension filters out empty strings (`if word != ''`)
    # list comprehension creates a new list based on the values of an existing list
    # if the word in string ISN'T an empty string

    # list comprehension version
    # words = [word for word in string.split(' ') if word != '']

     # split the string into a list of words
    words = string.split()

    # do we need to loop?
    # no, because we already have a clean list to return the length of
    return len(words)

print(word_count('hi     there')) # result: 2
print(word_count('hi there    ')) # result: 2
