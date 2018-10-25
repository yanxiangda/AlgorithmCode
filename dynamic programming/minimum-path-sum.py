
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
        # 二维List记录
        record = [[-1 for j in range(yMax + 1)] for i in range(xMax + 1)]
        return self.Optimization(grid, 0, 0, xMax, yMax, record)

    def Optimization(self, grid, x, y, xMax, yMax, record):
        recordResult = record[x][y]
        if recordResult != -1:
            return recordResult
        # 向右一步走
        # 判断是否超出
        if y == yMax:
            minRight = sys.maxsize
        else:
            minRight = self.Optimization(grid, x, y + 1, xMax, yMax, record)
        if x == xMax:
            minDown = sys.maxsize
        else:
            minDown = self.Optimization(grid, x + 1, y, xMax, yMax, record)
        minCurrent = minDown if minRight > minDown else minRight
        # 如果最小值是无穷，说明找到角落了
        currentValue = grid[x][y]
        if minCurrent == sys.maxsize:
            record[x][y] = currentValue
            return currentValue
        else:
            record[x][y] = currentValue + minCurrent
            return currentValue + minCurrent



