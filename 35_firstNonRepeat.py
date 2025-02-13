# more robust solution

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
    
    return -1  # Return -1 if no unique character is found

print(first_non_repeat('hih'))

# brute forc eapproach
def first_non_repeat(str):
    # loop through the range/string
    # this creates a range/numbers the length of the string
    # range generates a sequence of numbers from 0 to len(string) -1
    for i in range(len(str)):
        if str.count(str[i]) == 1:
            return str[i]

    return 'no non-repeating characters'

print(first_non_repeat('hih'))
