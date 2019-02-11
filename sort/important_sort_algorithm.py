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


# 归并排序
def mergesort(data, start, end):
    # 拆分为两个数组
    size = end - start + 1
    if size <= 1:
        return
    midIndex = start + int((size) / 2)
    mergesort(data, start, midIndex - 1)
    mergesort(data, midIndex, end)
    merge(data, start, midIndex - 1, midIndex, end)
    return data
    
# 归并过程，要使用临时的内存空间辅助排序
# 用index的方法进行排序
def merge(data, s1, e1, s2, e2):
    s = s1
    assist = []
    while ((s1 <= e1) & (s2 <= e2)):
        if (data[s1] <= data[s2]):
            assist.append(data[s1])
            s1 = s1 + 1
        else:
            assist.append(data[s2])
            s2 = s2 + 1
    # 对剩余的部分，直接加入即可
    if s1 > e1:
        assist.extend(data[s2:e2+1])
    else:
        assist.extend(data[s1:e1+1])
    # 将数据拷贝到原数据上
    for i in range(s, e2+1):
        data[i] = assist[i-s]

# 数据测试
data = [6,1,2,7,9,3,4,5,10,8]
print (data)
quicksort(data, 0, len(data)-1)
print (data)



