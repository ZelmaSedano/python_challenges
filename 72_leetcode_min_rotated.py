def leetcode_min_rotated(list):
    # edgecase: if list is empty
    if not list:
        return 'please add elements to list'

    # you want to rotate the list by whatever is the first number in the list
    # create a variable to hold that number
    index = list[0]

    # create a new list that is rotated by index
    # you want the last part of the original list + first part up to index
    arr = list[index: len(list)] + list[0:index]

    return arr

print(leetcode_min_rotated([3,4,5,6,7]))
