def findDivisors(num):
  result = []

  for i in range(2, num):
    if(num % i == 0):
      result.append(i)
  
  print(result)

findDivisors(72)
