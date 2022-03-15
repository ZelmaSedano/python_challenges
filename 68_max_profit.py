# leetcode problem: given a list of prices, with each element representing a workday
# return the maximum profit b/w stock prices (**you want to buy for less and sell for more)
# so, you want the smallest elements to be at the end of the list; if it's not, then there's not profit
def max_profit(prices):
    # prices = list
    # edgecase: if length of list if less than 1
        if len(prices) <= 1:
            return 0
        # if length of prices is only 2
        elif len(prices) == 2:
            # if 2nd element - 1st element is less than 0, return 0
            if prices[1] - prices[0] <= 0:
                return 0
            # if 2nd element - 1st element is larger than 0, return difference
            else:
                return prices[1] - prices[0]
            
        # create a variable that holds the profit     
        max_profit = 0
        # create a variable that holds the 1st element
        min_price = prices[0]
        
        # loop from 1 to end of list 
        for i in range(1,len(prices)):
            # if the current element is smaller than last 1st element
            if prices[i] < min_price:
                # if it is smaller, set the smallest price to be the current element
                min_price = prices[i]
            # else, if the current element - min_price is LARGER than max_profit
            elif prices[i] - min_price > max_profit:
                # set max_profit as current element - min_price
                max_profit = prices[i] - min_price
            
        return max_profit

print(max_profit([7,1,5,3,6,4]))
