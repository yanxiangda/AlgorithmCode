
# 爬楼梯



class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        iteratorResult = [-1 for i in range(n)]
        return self.iteratorCal(n, iteratorResult)
        
    def iteratorCal(self, n, iteratorResult):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if iteratorResult[n - 1] == -1:
            iteratorResult[n - 1] = self.iteratorCal(n - 1, iteratorResult) + self.iteratorCal(n - 2, iteratorResult)
        return iteratorResult[n - 1]
