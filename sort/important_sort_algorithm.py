# 快速排序
def quicksort(data, minIndex, maxIndex):
    if maxIndex - minIndex <= 0:
        return
    # 选取一个参考基准值，直接取队列的第一个
    baseIndex = minIndex
    fixIndex = maxIndex
    baseValue = data[baseIndex]
    # print ("fixIndex=%s" % maxIndex)
    # print ("baseIndex=%s" % baseIndex)
    while(True):
        # 左边先向右移动一格
        if data[minIndex] <= baseValue:
             minIndex = minIndex + 1
        elif data[maxIndex] >= baseValue:
            maxIndex = maxIndex - 1
        else:
            # 交换两个数的位置
            midValue = data[minIndex]
            data[minIndex] = data[maxIndex]
            data[maxIndex] = midValue         
        # 如果两个指针相遇，最后一次遍历
        if minIndex == maxIndex:
            if data[minIndex] < baseValue:
                data[baseIndex] = data[minIndex]
                data[minIndex] = baseValue
                quicksort(data, baseIndex, max(minIndex - 1, baseIndex))
                quicksort(data, min(minIndex + 1, fixIndex), fixIndex)
            else:
                data[baseIndex] = data[minIndex - 1]
                data[minIndex- 1] = baseValue
                quicksort(data, baseIndex, max(minIndex - 2, baseIndex))
                quicksort(data, min(minIndex, fixIndex), fixIndex)
            return
        

# 数据测试
data = [6,1,2,7,9,3,4,5,10,8]
print (data)
quicksort(data, 0, len(data)-1)
print (data)

