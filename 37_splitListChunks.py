def split_list_chunks(list, num=None):
    if not list and num is None:
        return 'please add arguments'
    if not list:
        return 'please add elements to list'
    if num is None:
        return 'please add a number to 2nd argument'

    # create a result variable to return
    result = []

    # loop through list using 0, len(list), num
    for i in range(0, len(list), num):
        result.append(list[i:i+num])

    return result

print(split_list_chunks([0,1,2,3,4,5], 2))
