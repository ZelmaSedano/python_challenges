def rotate_list_right(list, num):
    # edgecase: if list is empty or num is negative
    if not list and num < 0:
        return 'please add elements to list and make sure to use postiive numbers for 2nd arg'
    elif not list:
        return 'please add elements to list'
    elif num < 0:
        return 'please only use positive numbers for 2nd arg'

    result = list[len(list)-num:len(list)] + list[0:len(list)-num]
    return result

print(rotate_list_right([0,1,2,3,4], 1))
