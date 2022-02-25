def consecutive_ints(list):
    # check to make sure list isn't empty
    if not list:
        return 'please add items to list'

    # the extra -1 keeps 'out of range' from happening
    for i in range(list[0], list[-1]-1):
        if(list[i] == list[i+1]):
            bool = True
        else:
            bool = False
    return bool

print(consecutive_ints([1,3,3]))
