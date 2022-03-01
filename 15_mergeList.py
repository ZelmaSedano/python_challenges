def merge_lists(list1, list2):
    if not list1:
        return 'please add elements to list1'
    if not list2:
        return 'please add elements to list2'

    return list1 + list2

print(merge_lists([1,2,3], [4,5,6]))
