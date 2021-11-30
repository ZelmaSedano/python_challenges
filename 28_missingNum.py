def missingNum(arr):
  result = []
  for ele in range(arr[0], arr[-1]+1):
      if ele not in arr:
          result.append(ele)
  print(result)

missingNum([1,2,3,4,6])
