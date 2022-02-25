def consecutive_ints(list):
    if not list:
        return 'please add elements to your list'

    # loop through the list
    for i in range(list[0], list[-1]):
        if list[i] == list[i+1]:
            bool = True
        else:
            bool = False

    return bool

print(consecutive_ints([1,2,3,3]))
