def is_prime(num):
    # edgecases: if num is below 0 or 1, return message that negative numbers and 1 can't be prime
    if num < 0:
        return 'only positive numbers can be prime'
    if num == 1:
        return '1 is not a prime number'

    # loop from 2 to num, not including num
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(is_prime(17))
