def merge_and_sort(list1, list2):
    if not list1 and not list2:
        return 'please add arguments'
    if not list1:
        return 'please add elements to list1'
    if not list2:
        return 'please add elements to list2'

    return sorted(list1+list2)

print(merge_and_sort([1,2,3], [3,2,1]))
