
# 最长回文子序列

class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        strList = list(s)
        # 初始化一个二维list
        size = len(strList)
        # 初始化一个二维list
        recordResult = [[-1 for i in range(size)] for i in range(size)]
        return self.localCalculate(strList, 0, len(strList) - 1, recordResult)
        # print (recordResult)

    def localCalculate(self, strList, startIndex, endIndex, recordResult):
        haveValue = recordResult[startIndex][endIndex]
        if (haveValue != -1):
            return haveValue
        if (startIndex > endIndex):
            return 0
        if (startIndex == endIndex):
            return 1
        result = 0
        if (strList[startIndex] == strList[endIndex]):
            result = self.localCalculate(strList, startIndex + 1, endIndex - 1, recordResult) + 2
        else:
            rightMax = self.localCalculate(strList, startIndex + 1, endIndex, recordResult)
            leftMax = self.localCalculate(strList, startIndex, endIndex - 1, recordResult)
            if (rightMax > leftMax):
                result = rightMax
            else:
                result = leftMax
        recordResult[startIndex][endIndex] = result
        return result




