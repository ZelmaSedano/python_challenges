def findDuplicates(arr):
    result = []
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                result.append(arr[i])
    print(result)

findDuplicates([1,2,3,1,2])
