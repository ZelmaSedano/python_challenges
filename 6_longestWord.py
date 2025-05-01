def longest_word(string):
    # Step 1: Remove extra spaces at start and end
    string1 = string.strip()
    
    # Step 2: Split into words (automatically handles multiple spaces between words)
    words = string1.split()
    
    # Step 3: Check if we got any words
    if not words:  # If the list is empty
        return "No words found"
    
    # Step 4: Find the longest word
    longest = words[0]  # Start with the first word
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

# Test the function
print(longest_word('hi there     bub'))  # Output: 'there'
