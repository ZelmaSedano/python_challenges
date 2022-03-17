def split_list_chunks(list, num):
    # edgecase: if the length of list is less than num
    if len(list) < num:
        return 'please add more elements to list'
    # edgecase: if the list is empty
    if not list:
        return 'please add elements to list'
    # edgecase: if num is negative
    if num < 0:
        return 'please only use positive numbers'

    # create a result variable to add sublists to and return
    result = []

    # loop through list using 0, len(list), num
    for i in range(0, len(list), num):
        # add a sublist num length to result variable
        result.append(list[i:i+num])

    return result

print(split_list_chunks([0,1,2], 4))
