# check to see if there are two consecutive elements in an array
def consecutiveInts(arr):
  for i in range(len(arr) - 1):
    if(arr[i] == arr[i+1]):
      bool = True
    else:
      bool = False
  print(bool)


consecutiveInts([1,2,1])
