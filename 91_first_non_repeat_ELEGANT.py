def first_non_repeat(string):
    # create an empty list
    obj = {}

    # loop through the string, if the current element is in the list/obj, then add to its value
    for char in string:
        # check to see if char is in list
        if char in obj:
            arr[char] += 1
        else:
            arr[char] = 1

    # loop through the string
    for char in string:
        # if the current element is ALSO in array, and it's value is 1, return it
        if obj[char] == 1:
            return char
        
    # if there aren't any non-repeating chars
    return 'no non-repeating characters'

print(first_non_repeat('hi'))
