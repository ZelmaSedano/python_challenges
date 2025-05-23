def sorted_backwards(lst):
    # first sort the list
    lst1 = sorted(lst)

    return lst1[::-1]

print(sorted_backwards([3,33333,33,-2]))
