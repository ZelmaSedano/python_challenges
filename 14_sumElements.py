def sum_list(list):
    # edgecase: if list is empty
    if not list:
        return 'please add elements to list'

    # create a result variable
    result = 0

    # loop through list, adding to result with each loop
    for i in list:
        result += i

    return result

print(sum_list([1,2,3,4]))
