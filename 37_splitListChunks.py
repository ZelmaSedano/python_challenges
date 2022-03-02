def chunks(list, num=None):
    if not list:
        return 'please add elements to list'
    if num is None:
        return 'please add a number to 2nd arg'

    result = []
    # loop through list
    for i in range(0, len(list), num):
        result.append(list[i:i+num])

    return result

print(chunks([0,1,2,3,4,5], 2))
