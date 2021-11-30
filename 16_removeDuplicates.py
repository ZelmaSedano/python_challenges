def removeDuplicates(arr):
  res = []
  for i in arr:
    if i not in res:
      res.append(i)
  print(str(res))

removeDuplicates([1,2,3,4,1,2])
