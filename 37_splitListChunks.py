def split_list_chunks(list, num):
    # edgecases: if list is empty or num is negative
    if not list:
        return 'please add elements to list'
    if num < 0:
        return 'please only use positive numbers'

    # create a result list to return
    result = []

    # loop through the list using: 0, len(list), num
    for i in range(0, len(list), num):
        # add sections of the list to result using start:stop syntax
        result.append(list[i:i+num])

    return result

print(split_list_chunks([0,1,2,3,4,5], 2))
