def first_non_repeat(s):
    arr = {}  # Use a dictionary to store character counts
    
    # First loop: Count occurrences of each character
    for char in s:
        if char in arr:
            arr[char] += 1
        else:
            arr[char] = 1
    
    # Second loop: Find the first non-repeating character
    for char in s:
        if arr[char] == 1:  # Looking for a count of 1, not 2
            return char  # Return the first unique character
    
    # Return -1 if no unique character is found
    return 'no non-repeating characters'

print(first_non_repeat('hih'))
