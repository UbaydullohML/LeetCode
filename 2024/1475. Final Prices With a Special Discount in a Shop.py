# 1475. Final Prices With a Special Discount in a Shop
# Brute Force method
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)

        # start with original prices as final prices
        result = prices[:]
        for i in range(n):
            for j in range(i+1,n):

                # find first smaller or equal prices 
                if prices[j] <= prices[i]:
                    result[i] -= prices[j] # apply discount
                    break
        return result
        
