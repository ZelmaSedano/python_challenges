# create a function that returns the numbers from an array that add up to target
def twoSum(arr, target):
    for i in range(len(arr)-1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [arr[i], arr[j]]


print(twoSum([1,2,3,4,5], 8))
