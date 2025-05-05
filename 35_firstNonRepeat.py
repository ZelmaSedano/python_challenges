def first_non_repeat_brute(string):
    # remove spaces? - remove all spaces
    # split? naw

    string1 = string.replace(' ', '')

    # loop through new string 
    # do we need to access indices? - NO
    for i in string1:
        if string1.count(i) == 1:
            return i
        
    # if there are no non-repeating characters
    return 'no non-repeating characters'

print(first_non_repeat_brute('hi therei'))
