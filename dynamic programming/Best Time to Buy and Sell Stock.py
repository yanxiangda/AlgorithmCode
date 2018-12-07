# 买卖股票的最佳时机

# Method1 传统动态规划方法，AC 199/200
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.localProfit(prices,(0, len(prices) - 1))

    def localProfit(self, prices, ind):
        if (ind[0] >= ind[1]):
            return 0
        a = self.localProfit(prices, (ind[0], ind[1] - 1))
        b = self.localProfit(prices, (ind[0] + 1, ind[1]))
        c = prices[ind[1]] - prices[ind[0]]
        return max(a, b, c, 0)
        


# Method2 AC全部
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size <= 1:
            return 0
        lastMin = prices[0]
        currentMax = 0
        for i in range(1, size):
            currentMax = max(currentMax, prices[i] - lastMin)
            if prices[i] < lastMin:
                lastMin = prices[i]
        return currentMax
      
