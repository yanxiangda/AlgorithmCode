
# 最长回文子串


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        strList = list(s)
        # 初始化一个二维list
        size = len(strList)
        if size == 0 :
            return ""
        # 初始化一个二维list
        recordResult = [[-1 for i in range(size)] for i in range(size)]
        self.localCalculate(strList, 0, len(strList) - 1, recordResult)
        # 遍历寻找最优
        maxValue = -1
        maxX = -1
        maxY = -1
        for i in range(size):
            for j in range(size):
                if ((j-i+1) > maxValue) & (recordResult[i][j] == 1):
                    maxValue = j-i+1
                    maxX = i
                    maxY = j
        return (''.join(strList[maxX:maxY+1]))

    def localCalculate(self, strList, startIndex, endIndex, recordResult):
        # print (strList[startIndex:endIndex+1])
        # 判断当前是否计算过
        # 0表示不是、-1表示没计算过、1表示是
        haveValue = recordResult[startIndex][endIndex]
        # 如果计算过，直接返回结果即可
        if haveValue != -1:
            return haveValue
        if (startIndex > endIndex):
            return 1
        if (startIndex == endIndex):
            recordResult[startIndex][endIndex] = 1
            return 1
        result = 0
        # 与最长子序列不同，回文子串不存在贪婪最优，所以三种情况都要计算
        if ((strList[startIndex] == strList[endIndex]) & (self.localCalculate(strList, startIndex + 1, endIndex - 1, recordResult) == 1)):
            result = 1
        else:
            result = -1
            rightMax = self.localCalculate(strList, startIndex + 1, endIndex, recordResult)
            leftMax = self.localCalculate(strList, startIndex, endIndex - 1, recordResult)
        recordResult[startIndex][endIndex] = result
        return result



