def word_count(string):
    # loop through the split string, (' ') removes spaces
    # if the word isn't a space, add it to words list/array
    # 2. The list comprehension filters out empty strings (`if word != ''`)
    # list comprehension creates a new list based on the values of an existing list
    # if the word in string ISN'T an empty string
    words = [word for word in string.split(' ') if word != '']
    
    # Return the count of remaining valid words
    return words

print(word_count('hi there    '))  
