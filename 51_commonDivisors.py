def common_divisors(num1, num2):
    # edgecase: if both numbers aren't negative or positive
    if num1 < 0 and num2 > 0:
        return 'please only use positive or negative numbers'
    if num1 > 0 and num2 < 0:
        return 'please only use positive or negative numbers'

    # create a result list to return
    result = []

    # loop from 2 to num2, including num2
    for i in range(2, num2+1):
        if num1 % i == 0 and num2 % i == 0:
            result.append(i)

    return result

print(common_divisors(15,30))
