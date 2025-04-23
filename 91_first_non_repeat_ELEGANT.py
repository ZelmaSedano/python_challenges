def first_non_repeat(string):
    # Create a dictionary to count character occurrences
    char_count = {}
    
    # First pass: count each character's occurrences
    for char in string:
        # if char is present in char_count list, += 1 to it
        if char in char_count:
            char_count[char] += 1
        # if char isn't present in char_count list, add it with a value of 1
        else:
            char_count[char] = 1
    
    # Second pass: find the first character with count 1
    for char in string:
        if char_count[char] == 1:
            return char
    
    return 'no non-repeating chars'

print(first_non_repeat('hii'))  # Should return 'h'
print(first_non_repeat('hello'))  # Should return 'h'
print(first_non_repeat('aabbcc'))  # Should return 'no non-repeating chars'
