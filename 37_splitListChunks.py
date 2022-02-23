def chunks (list, n):
    new_list = []
    for i in range(0, len(list), n):
        new_list.append(list[i:i+n])

    return new_list

print(chunks([1,2,3,4,5,6], 2))
