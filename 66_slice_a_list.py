def slice_list(list, start, stop):
    # edgecase: if list is empty or start and stop are negative numbers
    if not list:
        return 'please add elements to list'
    if start < 0 or stop < 0:
        return 'only positive numbers can be used as arguments'

    # return the sliced list
    return list[start:stop]

print(slice_list([0,1,2,3,4,5], 0, 3))
