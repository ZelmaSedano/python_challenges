def maxSubArray(nums):
    # create a variable that holds the max number from list
    ans = max(nums)
    # create a variable and set it to 0
    a = 0

    # loop through list
    for i in nums:
        # if a is under 0, a is 0
        if a<0: a=0 
        
        # set a to be itself plus i
        a += i

        # set ans to be the max b/w a & ans
        ans = max(a,ans)

        
    return ans

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
