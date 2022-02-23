def countOccurrence(arr, element):
    if len(arr) == 0:
        print('please add elements to list')
    count = 0
    for i in arr:
        if(i == element):
            count+=1
    return count

print(countOccurrence([1,2,3],3))
