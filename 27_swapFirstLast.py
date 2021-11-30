def swapFirstLastElement(str):
  arr = list(str)

  arr[0], arr[-1] = arr[-1], arr[0]

  return ''.join(arr)


print(swapFirstLastElement('hi'))
