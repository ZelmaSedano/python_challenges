def list_has_element(list, item):
    # edgecase: if list is empty or item is negative number
    if not list:
        return 'please add elements to list'
    elif item < 0:
        return 'please only use positive numbers'

    # check to see if item is list and return result
    return item in list

print(list_has_element([1,2,3,4], 5))
