def max_profit(prices):
    # Edge case: if there's less than 2 days of data, 
    # we can't make any transactions (need at least 1 buy and 1 sell)
    if len(prices) < 2:
        return 0
    
    # Initialize variables:
    # min_price tracks the lowest price we've seen so far
    # max_profit tracks the highest profit we can make
    min_price = prices[0]  # Start with first day's price
    max_profit = 0         # Initialize with 0 profit
    
    # Loop through each day's price starting from the second day
    for price in prices[1:]:
        # Update min_price if we find a new lowest price
        # This represents the best day to buy so far
        if price < min_price:
            min_price = price
        
        # Calculate how much profit we'd make if we sold today
        current_profit = price - min_price
        
        # Update max_profit if selling today would give better profit
        if current_profit > max_profit:
            max_profit = current_profit
    
    # After checking all days, return the maximum profit found
    # (will be 0 if prices only decreased)
    return max_profit

# Test Case 1: Normal case with profit opportunity
# Buy at 1 (day 2), sell at 6 (day 5) → profit 5
print(max_profit([7,1,5,3,6,4]))  # Output: 5

# Test Case 2: Prices only decreasing - no profit possible
print(max_profit([7,6,4,3,1]))     # Output: 0

# Test Case 3: Price fluctuates but best is buy at 2, sell at 4
print(max_profit([2,4,1]))         # Output: 2
