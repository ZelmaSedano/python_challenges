def twoSum(arr, target):
  result = []
  
  for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == target:
        result.append([arr[i], arr[j]])
  print(result)

twoSum([1,2,3,4,5], 8)
