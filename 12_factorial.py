def factorial(num):
  factorial = 1

  if num < 0:
    print('Sorry, factorial does not exist for numbers')
  elif num == 0:
    print('The factorial of 0 is 1')
  else:
    for i in range(1, num+1):
      factorial = factorial * i
    print('The factorial is ', factorial)

factorial(5)
