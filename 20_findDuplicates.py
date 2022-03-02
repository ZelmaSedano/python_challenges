def find_dupes(list):
    # create a result list to return
    result = []

    # loop through the list
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                result.append(list[i])

    if len(result) == 0:
        return 'no duplicates'
    else:
        return set(result)

print(find_dupes([1,2,3,3,4,4,4,4]))
