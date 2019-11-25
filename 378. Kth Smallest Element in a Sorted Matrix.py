# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.
# 方法一
# 先加一个数，每次一层层加
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if k > len(matrix)*len(matrix[0]):
            return None
        q = []
        heapq.heappush(q, (matrix[0][0],0,0))
        count = 0
        index = {}
        index[(0,0)] = True
        while True :
            size = len(q)
            for ele in range(size):
                count += 1
                res,i,j = heapq.heappop(q)
                if count == k:
                    return res
                if (i+1,j) not in index and i+1 < len(matrix) and j < len(matrix[0]):
                    heapq.heappush(q,(matrix[i+1][j],i+1,j))
                    index[(i+1,j)] = True
                if (i,j+1) not in index and i < len(matrix) and j+1 < len(matrix[0]):
                    heapq.heappush(q,(matrix[i][j+1],i,j+1))
                    index[(i,j+1)] = True
# 先加一列，然后每次横着加



#heap方法

import heapq
class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        if matrix is None or len(matrix) == 0:
            return None
        if k == 0:
            return None
        if k == 1:
            return matrix[0][0]
        array = []
        result = []
        count = 1
        heapq.heappush(array, (matrix[0][0], 0, 0))
        while count <= k:
            pop = heapq.heappop(array)
            if pop[2] + 1 < len(matrix[0]) and (matrix[pop[1]][pop[2] + 1], pop[1], pop[2] + 1) not in array:
                heapq.heappush(array, (matrix[pop[1]][pop[2] + 1], pop[1], pop[2] + 1))
            if pop[1] + 1 < len(matrix) and (matrix[pop[1] + 1][pop[2]], pop[1] + 1, pop[2]) not in array:
                heapq.heappush(array, (matrix[pop[1] + 1][pop[2]], pop[1] + 1, pop[2]))
            count += 1
        return pop[0]
#二分法
class Solution1:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def __init__(self):
        self.num = 0
        self.exists = None
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        m = len(matrix[0])
        left = matrix[0][0]
        right = matrix[n-1][m-1]
        while left <= right:
            mid = (right+left)/2
            type = self.helper(mid,matrix)
            if type[1] and type[0] == k:
                return mid
            elif type[0] < k:
                left = mid + 1
            else:
                right = mid - 1
        return left
    def helper(self, value, matrix):
        n = len(matrix)
        m = len(matrix[0])
        exists = False
        num = 0
        i = n - 1
        j = 0
        while i >= 0 and j < m:
            if matrix[i][j] == value:
                exists = True
            if matrix[i][j] <= value:
                num += i + 1
                j += 1
            else:
                i -= 1
        return (num,exists)


class ValueIndex:
    def __init__(self, val, x, y):
        self.x = x
        self.y = y
        self.val = val

    def __lt__(a, b):
        return a.val < b.val


class Solution5:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        m = len(matrix[0])
        value_min_heap = []
        ele = ValueIndex(matrix[0][0], 0, 0)
        pos_set = set()
        heapq.heappush(value_min_heap, ele)
        pos_set.add((0, 0))
        while k > 0:
            if len(value_min_heap) == 0:
                return False
            cur = heapq.heappop(value_min_heap)
            if cur.x + 1 < n and (cur.x + 1, cur.y) not in pos_set:
                next = ValueIndex(matrix[cur.x + 1][cur.y], cur.x + 1, cur.y)
                heapq.heappush(value_min_heap, next)
                pos_set.add((cur.x + 1, cur.y))
            if cur.y + 1 < m and (cur.x, cur.y + 1) not in pos_set:
                next = ValueIndex(matrix[cur.x][cur.y + 1], cur.x, cur.y + 1)
                heapq.heappush(value_min_heap, next)
                pos_set.add((cur.x, cur.y + 1))
            k -= 1
        return cur.val


class ValueIndex:
    def __init__(self, val, x, y):
        self.x = x
        self.y = y
        self.val = val

    def __lt__(a, b):
        return a.val < b.val


class Solution4:
    def kthSmallest(self, matrix,k):
        n = len(matrix)
        m = len(matrix[0])
        value_min_heap = []
        for i in range(len(matrix)):
            ele = ValueIndex(matrix[i][0], i, 0)
            heapq.heappush(value_min_heap, ele)
        while len(value_min_heap):
            cur = heapq.heappop(value_min_heap)
            if k == 1:
                return cur.val
            if cur.y + 1 < m:
                next = ValueIndex(matrix[cur.x][cur.y + 1], cur.x, cur.y + 1)
                heapq.heappush(value_min_heap, next)
            k -= 1
        return -1



if __name__ == "__main__":


    # A = [[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]
    # k = 19
    # A = [[-5]]
    # k = 1
    A = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8

    s = Solution4()

    print(s.kthSmallest(A,k))
