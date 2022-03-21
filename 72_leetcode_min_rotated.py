def leetcode_find_min_rotated_array(list):
    # edgecase: if list is empty
    if not list:
        return 'please add elements to list'

    # select and save the 1st element's value from the list
    index = list[0]

    # slice the array at whichever index is the first element's value
    list = list[index:len(list)] + list[0:index]

    return min(list)

print(leetcode_find_min_rotated_array([3,4,5,6,7]))
