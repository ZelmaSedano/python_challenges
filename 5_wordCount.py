def word_count(string):
    # split on single spaces and filter out empty strings
    words = [word for word in string.split(' ') if word != '']
    
    # return the length of the list
    return len(words)

print(word_count('hi there    '))  # Output: 2
