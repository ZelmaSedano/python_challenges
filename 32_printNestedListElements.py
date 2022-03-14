def print_nested_list(list1):
    # edgecase: if list is empty
    if not list:
        return 'please add elements to list'

    # loop through the list
    for i in list1:
        # if current element is a list, loop through it using j
        if isinstance(i, list):
            for j in i:
                # print out j
                print(j)
        # if current element ISN'T a list, simply print i
        else:
            print(i)

print_nested_list([1,2,3,[4,5,6,[7]]])
