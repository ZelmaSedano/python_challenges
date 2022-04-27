def missing_num(list):
    # edgecase: if list is empty
    if not list:
        return 'please add elements to list'
    # loop through list using index
    # the reason you don't have to use len(list)-1 is because you're not comparing the current element w/ the next element
    for i in list:
        # list[i+1] = next element in list
        # list[i]+1 = value + 1
        # if the next element in list is NOT current element's value + 1
        if list[i+1] != list[i]+1:
            # return current element's value + 1
            return list[i]+1

print(missing_num([1,2,3,4,6]))
