def missing_num(list):
    # check to make sure arr isn't empty
    if not list:
        return 'please add items to your list'
    
    # make sure to start from 0 to last element, otherwise it won't work
    for i in range(list[0], list[-1]):
        if i not in list:
            return i
            

    return 'no missing numbers'

print(missing_num([1,2,3,4,6]))
