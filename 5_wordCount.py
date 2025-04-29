def word_count(string):
    # loop through the split string, (' ') removes spaces
    # if the word isn't a space, add it to words list/array
    # 2. The list comprehension filters out empty strings (`if word != ''`)
    # list comprehension creates a new list based on the values of an existing list
    # if the word in string ISN'T an empty string

    # list comprehension version
    # words = [word for word in string.split(' ') if word != '']

    # create an empty array/list, which we'll push letters/words into
    words = []

    # loop through the split string
    for word in string.split(' '):
        if word != '':
            words.append(word)
    # if word isn't a space, add it to a new array called 'words'
    
    # return the length of words array/list
    return len(words)

print(word_count('hi there    ')) 
