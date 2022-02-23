def find_dupes(list):
    new_list = []
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                new_list.append(list[i])

    return new_list

print(find_dupes([1,2,3,1]))
