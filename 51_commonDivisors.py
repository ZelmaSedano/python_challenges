def common_divisors(num1, num2):
    # edgecase: if one number is negative
    if num1 > 0 and num2 < 0:
        return 'please use only positive or negative numbers'
    elif num1 < 0 and num2 > 0:
        return 'please use only positive or negative numbers'
    
    # create a variable to return
    result = []

    # loop through list
    for i in range(2, num2+1):
        if(num1 % i == 0 and num2 % i == 0):
            result.append(i)

    return result

print(common_divisors(15,30))
