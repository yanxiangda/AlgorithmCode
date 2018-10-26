
# 连续的子数组和

class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        size = len(nums)
        record = [[None for j in range(size)] for i in range(size)]
        if self.Optimization(nums, k, 0, size - 1, record) == -2:
            return True
        else:
            return False
    '''
    start和end表示索引
    应该避免的是多次求和的计算，而不用避免判断是否为k的倍数的运算
    缓存数组里面存的一定都是数字，都是不是结果的数字
    数组和k都是非负的，所以注意0的情况处理
    还有一个要求，子数组大小至少为2
    还有一个坑，k是整数，不一定都是大于0的
    '''
    def Optimization(self, nums, k, start, end, record):
        if start > end:
            return 0
        if start == end:
            return nums[start]
        haveValue = record[start][end]
        if haveValue != None:
            return haveValue 
        rightSum = self.Optimization(nums, k, start + 1, end, record)
        if (rightSum == -2):
            return -2
        leftSum = self.Optimization(nums, k, start, end - 1, record)
        if (leftSum == -2):
            return -2
        currentValue = nums[start] + rightSum
        if currentValue == 0:
            return -2
        if k == 0:
            record[start][end] = currentValue
            return currentValue
        if currentValue % abs(k) == 0:
            return -2
        else:
            record[start][end] = currentValue
            return currentValue




