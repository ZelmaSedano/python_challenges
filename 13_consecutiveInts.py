def consecutive_ints(list):
    # edge case: if list is empty
    if not list:
        return 'please add items to your list'

    for i in range(len(list)-1):
        if(list[i] == list[i+1]):
            bool = True
        else:
            bool = False
    # make sure this is out of loop, otherwise it'll return False if the first two elements don't match
    return bool

print(consecutive_ints([1,2,3,1,2,3,3,3]))
