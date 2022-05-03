def consectutive_ints(list):
    # edgecase: if list is empty
    if not list:
        return 'please add elements to list'

    # make a range from 0 to length of list
    # -1 to keep 'out of range' error occurring
    # if you use 'for i in list', it will error when there are no consecutive elements
    for i in range(0, len(list)-1):
        # if the current element and the next element are the same, return True
        if list[i] == list[i+1]:
            return True
    
    return False

print(consectutive_ints([1,2,3,4]))
