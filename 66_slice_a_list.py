# slice a list at a certain stop and start point
def slice_list(list, start, stop):
    # edgecases: if list is empty, if start is negative, and stop is negative or past edge
    if not list:
        return 'please add elements to list'
    if start < 0:
        return 'please only use positive numbers'
    if stop < 0:
        return 'please only use positive numbers'
    if stop > len(list):
        return 'please use a smaller number, the list is not list long'

    return list[start:stop]

print(slice_list([1,2,3,4,5], 0, 7))
