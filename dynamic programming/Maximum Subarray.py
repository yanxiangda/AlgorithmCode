
# 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        resSum = 0
        for i in nums:
            if resSum > 0:
                resSum = resSum + i
            else:
                resSum = i
            res = max(res, resSum)
        return res