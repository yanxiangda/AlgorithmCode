
# 最小路径和

import sys
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xMax = len(grid) - 1
        yMax = len(grid[0]) - 1
        return self.Optimization(grid, 0, 0, xMax, yMax)

    def Optimization(self, grid, x, y, xMax, yMax):
        # 向右一步走
        # 判断是否超出
        if y == yMax:
            minRight = sys.maxsize
        else:
            minRight = self.Optimization(grid, x, y + 1, xMax, yMax)
        if x == xMax:
            minDown = sys.maxsize
        else:
            minDown = self.Optimization(grid, x + 1, y, xMax, yMax)
        minCurrent = minDown if minRight > minDown else minRight
        # 如果最小值是无穷，说明找到角落了
        currentValue = grid[x][y]
        if minCurrent == sys.maxsize:
            return currentValue
        else:
            return currentValue + minCurrent


grid = [[1,3,1], [1,5,1], [4,2,1]] 
s = Solution()
s.minPathSum(grid)

