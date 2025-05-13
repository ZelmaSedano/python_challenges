def productExceptSelf(nums):
        # Initialize a result array filled with 1's (same length as nums)
        # Example: If nums = [1, 2, 3, 4], result starts as [1, 1, 1, 1]
        result = [1] * len(nums)

        # Outer loop: Iterate over each index 'i' in nums
        # This index 'i' is the position we're calculating the product for
        for i in range(len(nums)):
            
            # Inner loop: Iterate over each index 'j' in nums
            # This checks all other elements to multiply into result[i]
            for j in range(len(nums)):
                
                # Skip multiplying when i == j (we want product *except* nums[i])
                if i != j:
                    # Multiply result[i] by nums[j] (accumulates the product of all other elements)
                    result[i] *= nums[j]

        # Return the final result array
        # Example: For nums = [1, 2, 3, 4], result becomes [24, 12, 8, 6]
        return result

print(productExceptSelf([1,2,3,4]))
