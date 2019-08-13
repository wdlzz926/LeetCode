class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        if not prices:
            return 0
        minprice = prices[0]
        for i in prices:
            if i < minprice:
                minprice = i
            elif i-minprice > maxprofit:
                maxprofit = i-minprice
        return maxprofit