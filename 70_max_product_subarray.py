def maxProduct(list):
    # create a maximum product variable set to the first element
    max_product = list[0] 
    # create a minimum product variable and set it to 1st element
    min_product = list[0]
    # create a result variable, and set it to whatever max_product is
    result = max_product

    # loop through list
    for i in range(1,len(list)):
        # create a current variable and set it to list[i]
        curr = list[i]
        
        # create a temp_max variable and set it to whatever is the max: current element, max_product*current, or min_product * current
        temp_max = max(curr , max_product*curr , min_product*curr)

        # reset the min_product to be the minimum of: current element, max_product*current, or min_product*current
        min_product = min(curr , max_product*curr , min_product*curr)

        # reset max_product to be temp_max
        max_product = temp_max
        
        # reset result to be the maximum of: max_product or result
        result = max(max_product , result)
    
    # return result
    return result

print(maxProduct([2,3,-2,4]))
