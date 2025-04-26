def word_count(string):
    # Split the string into a list of words, handling empty strings:
    # 1. `string.split(' ')` splits on individual spaces, creating empty strings 
    #    for consecutive/multiple spaces (e.g., 'hi   there' → ['hi', '', '', 'there'])
    # 2. The list comprehension filters out empty strings (`if word != ''`)
    words = [word for word in string.split(' ') if word != '']
    
    # Return the count of remaining valid words
    return len(words)

# Test case: Trailing spaces demonstrate whitespace handling
print(word_count('hi there    '))  # Output: 2
