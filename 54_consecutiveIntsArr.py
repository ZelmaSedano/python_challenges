def consecutive(arr):
    res = []
    for i in range(0, len(arr)-1):
        if arr[i+1] == arr[i]:
            res.append(True)

    return True in res

print(consecutive([1,1,1]))
