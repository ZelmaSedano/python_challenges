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

    string1 = string.split(' ')
    # loop through the string
    for i in string1:
        if i != '':
            words.append(i)

    return len(words)

print(word_count('hi there'))

print(word_count('hi there    ')) 
