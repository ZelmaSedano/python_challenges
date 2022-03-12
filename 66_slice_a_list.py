def slice_list(list=None, start=None, stop=None):
    if list is None and start is None and stop is None:
        return 'please add arguments'
    if not list:
        return 'please add elements to list'

    return list[start:stop]

print(slice_list([0,1,2,3,4,5], 0, 3))
