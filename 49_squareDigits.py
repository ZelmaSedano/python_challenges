def common_divisors(num1, num2):
    # edgecases: if both nums aren't negative or positive
    if num1 < 0 and num1 > 0:
        return 'please only use positive or negative numbers'
    elif num1 > 0 and num2 < 0:
        return 'please only use positive and negative numbers'

    # create a result variable to add divisors to
    result = []

    # loop from 2 to num2, including num2
    for i in range(2, num2+1):
        # if i divides into num1 and 2, add to result
        if num1 % i == 0 and num2 % i == 0:
            result.append(i)

    # if result is empty, return no common divisors
    if len(result) == 0:
        return 'no common divisors'
    else:
        return result

print(common_divisors(15,30))
