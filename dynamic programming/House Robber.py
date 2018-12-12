# 打家劫舍

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        fnums = [0, 0, 0]
        fnums.extend(nums)
        sumFnums = [0 for _ in fnums]
        for i in range(3, size + 3):
            sumFnums[i] = max(fnums[i] + sumFnums[i - 2], fnums[i] + sumFnums[i - 3])
        return max(sumFnums[-1], sumFnums[-2])
            


