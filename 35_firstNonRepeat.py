def firstNonRepeat(str):
    if not str or str.isspace():
        return 'please add letters to your string'
    
    # create an empty list to keep the characters in order, b/c python doesn't keep them in their original order
    order = []
    # create an empty dictionary to hold the characters
    chars = {}

    # loop through the str
    for c in str:
        # if c is already in chars dict, add to its value by 1
        if c not in chars:
            chars[c] = 1
            order.append(c)
        else:
            chars[c] += 1
    # print(order)
    # print(chars)

    # loop through order list
    for c in order:
        # if the value of c in dictionary is 1
        if chars[c] == 1:
            return c

    #backup 
    return 'no non-repeating characters'

print(firstNonRepeat('hi'))
