def common_divisors(num1, num2):
    # edgecase: if one number is positive and one is negative, they aren't divisors
    if num1 < 0 and num2 > 0:
        return 'please only use positive numbers'
    elif num1 > 0 and num2 < 0:
        return 'please only use positive numbers'

    # create a result variable to return
    result = []

    # loop from 2 to num2, including num2
    for i in range(1, num2+1):
        if num1 % i == 0 and num2 % i == 0:
            result.append(i)

    return result

print(common_divisors(6, 18))
