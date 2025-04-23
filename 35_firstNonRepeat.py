# brute force - not as effcient
def first_non_repeat(string):
    # I like the brute-force approach
    # if there's only one of the letters in the entire string, then it is the first-non-repeating since it'll be the first to return

    # loop through the string
    for i in string:
        # if the current element's value count is 1, return it
        # it'll be the first non-repeat since we're looping through
        if string.count(i) == 1:
            return i
            
    # EVEN SIMPLER, no math logic
    for num in list:
        if num+1 not in list:
            return num+1
        
    # if there are no non-repeating chars
    return 'no non-repeating characters'

print(first_non_repeat('nono'))

# more efficient & less bulky
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
