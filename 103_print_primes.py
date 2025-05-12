def print_primes(num1, num2):
    result = []
    
    # Loop through the range of numbers
    for i in range(num1, num2):
        flag = 0  # Reset flag for each number
        
        # Check divisors from 2 to i-1
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break  # Not prime, exit inner loop
        
        # If prime (flag remains 0 and i > 1)
        if i > 1 and flag == 0:
            result.append(i)
    
    return result

# Test case
print(print_primes(3, 17))  # Output: [3, 5, 7, 11, 13]
