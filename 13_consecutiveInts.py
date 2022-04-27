def consecutive_ints(list):
    # edgecase: if list is empty
    if not list:
        return 'please add elements to list'

    # loop through list
    for i in list:
        # if the current element is the same as the next element, return true
        if list[i] == list[i+1]:
            return True

    return False

print(consecutive_ints([1,2,3,3]))
