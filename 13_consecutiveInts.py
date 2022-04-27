def consecutive_elements(list):
    # edgecase: if list is empty
    if not list:
        return 'please add elements to list'

    # create a range from 0 to length of list, -1 (so it doesn't return an 'out of range' error)
    for i in range(0, len(list)-1):
        # if the current element is the same as the next element, return true
        if list[i] == list[i+1]:
            return True

    # backup: return False if no consecutive elements
    return False

print(consecutive_elements([0,1,2,3,3]))
