def merge_and_sort(list1, list2):
    newList = list1+list2
    return sorted(newList)

print(merge_and_sort([1,2,3], [3,2,1]))
