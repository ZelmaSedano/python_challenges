def isNumPrime(num):
  if num > 1:
    for i in range(2, num):
      if(num % i ==0):
        print('is not a prime')
        break
      if(num % i != 0):
        print('is a prime')
        break


isNumPrime(6)
