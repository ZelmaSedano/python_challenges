def find_divisors(num=None):
    if num == None:
        return 'please enter a number'

    # create an empty list to hold divisors
    result = []

    # loop from 2 to num, not including num
    for i in range(2, num):
        if num % i == 0:
            result.append(i)

    if len(result) == 0:
        return 'no divisors, number is prime'
    else:
        return result

print(find_divisors())
