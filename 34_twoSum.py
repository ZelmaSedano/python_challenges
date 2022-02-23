def twoSum(list, target):
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                return [list[i], list[j]]

print(twoSum([1,2,3,4,5], 7))
