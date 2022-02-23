def missing_num(arr):
    list = []
    for i in range(arr[0], arr[-1]+1):
        if i not in arr:
            list.append(i)
    
    return list
    
print(missing_num([1,2,3,5]))
