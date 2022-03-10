def print_nested_list(arr=None):
    if arr is None:
        return 'please add a list'
    if not arr:
        return 'please add elements to list'

    # loop through list
    for i in arr:
        # if the current element is a list
        if isinstance(i, list):
            # loop through that list
            for j in i:
                print(j)
        else:
            print(i)

print_nested_list([1,2,3,[4, 5, [6]]])
