def find_divisors(num = None):
    if num is None:
        return 'please add an argument'

    # since we are returning multiple divisors, we should add them to a list:
    result = []

    for i in range(2, num):
        if(num % i == 0):
            result.append(i)

    return result

print(find_divisors(72))
