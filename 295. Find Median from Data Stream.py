import heapq
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []
    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.left == [] or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        if len(self.left)+2  == len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))
        elif len(self.left)==len(self.right)+2:
            heapq.heappush(self.right, -heapq.heappop(self.left))
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) == len(self.right):
            return (-self.left[0]+self.right[0]) / 2.0
        elif len(self.left) == len(self.right) + 1:
            return -float(self.left[0])
        else:
            return float(self.right[0])




#
# 数字是不断进入数组的，在每次添加一个新的数进入数组的同时返回当前新数组的中位数。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 说明
# 中位数的定义：
#
# 中位数是排序后数组的中间值，如果有数组中有n个数，则中位数为A[(n-1)/2]。
# 比如：数组A=[1,2,3]的中位数是2，数组A=[1,19]的中位数是1。
# 样例
# 持续进入数组的数的列表为：[1, 2, 3, 4, 5]，则返回[1, 1, 2, 2, 3]
#
# 持续进入数组的数的列表为：[4, 5, 1, 3, 2, 6, 0]，则返回 [4, 4, 4, 3, 3, 3, 3]
#
# 持续进入数组的数的列表为：[2, 20, 100]，则返回[2, 2, 20]


import heapq
class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """

    def __init__(self):
        self.num_of_ele = 0
        self.min_heap = []
        self.max_heap = []
    def medianII(self, nums):
        result = []
        for j in range(0, len(nums)):
            self.add_num(nums[j])
            result.append(self.get_med())
        return result

    def add_num(self, value):
        heapq.heappush(self.max_heap,-value)
        if self.num_of_ele % 2 == 0:
            if len(self.min_heap) == 0:
                self.num_of_ele += 1
                return
            elif -self.max_heap[0] > self.min_heap[0]:
                max_heap_root = -heapq.heappop(self.max_heap)
                min_heap_root = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -min_heap_root)
                heapq.heappush(self.min_heap, max_heap_root)
        else:
            heapq.heappush(self.min_heap, (-heapq.heappop(self.max_heap)))
        self.num_of_ele += 1

    def get_med(self):
        return -self.max_heap[0]

import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # max_heap
        self.small_heap = []
        # min_heap
        self.large_heap = []
        heapq.heapify(self.small_heap)
        heapq.heapify(self.large_heap)

    def addNum(self, num: int) -> None:
        # 如果small是空或者比small里最大的小，放small里， 否则放large里
        if len(self.small_heap) == 0 or num < -self.small_heap[0]:
            heapq.heappush(self.small_heap, -num)
        else:
            heapq.heappush(self.large_heap, num)
        # 如果是中间态，调整成稳定态
        if len(self.small_heap) + 1 == len(self.large_heap):
            heapq.heappush(self.small_heap, -heapq.heappop(self.large_heap))
        elif len(self.small_heap) == len(self.large_heap) + 2:
            heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))

    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.large_heap):
            return (-self.small_heap[0] + self.large_heap[0]) / 2
        else:
            return -float(self.small_heap[0])


import heapq


class MedianFinder2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # max_heap
        self.small_heap = []
        # min_heap
        self.large_heap = []
        # heapq.heapify(self.small_heap)
        # heapq.heapify(self.large_heap)

    def addNum(self, num: int) -> None:
        # 无脑加入small里
        heapq.heappush(self.small_heap, -num)
        # 在无脑从small里挤一个出来进large
        heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))
        # 再检查，如果large长，就在调整长度，保证small长（稳定态）
        if len(self.small_heap) < len(self.large_heap):
            heapq.heappush(self.small_heap, -heapq.heappop(self.large_heap))

    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.large_heap):
            return (-self.small_heap[0] + self.large_heap[0]) / 2
        else:
            return -float(self.small_heap[0])





# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



if __name__ == '__main__':

    obj = MedianFinder2()
    print(obj.addNum(-1))
    print(obj.findMedian())
    print(obj.addNum(-2))
    print(obj.findMedian())
    print(obj.addNum(-3))
    print(obj.findMedian())
    print(obj.addNum(-4))
    print(obj.findMedian())
    print(obj.addNum(-5))
    print(obj.findMedian())
    # obj.addNum(4)
    print(obj.findMedian())
