def rotate_list(list, num):
    # edgecases: if list is empty or num is negative
    if not list:
        return 'please add elements to list'
    if num < 0:
        return 'please only use positive numbers'

    # using the number, rotate the list
    result = list[num:len(list)] + list[0:num]

    return result

print(rotate_list([0,1,2,3,4,5], 3))
