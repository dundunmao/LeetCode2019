
# 最后结果
import bisect
class Solution1:
    def oddEvenJumps(self, A):
        n = len(A)
        odd_jump = [False] * n
        even_jump = [False] * n
        bst = SortedArray()
        # base case
        odd_jump[n - 1] = True
        even_jump[n - 1] = True
        bst.put(A[n - 1], n - 1)
        # general case
        for i in range(n - 2, -1, -1):
            # odd跳的结果 （比它大的里面找最小的）
            next_node = bst.find_next(A[i])
            odd_jump[i] = next_node[0] != -1 and even_jump[next_node[1]]
            # even跳的结果（比它小的里面找最大的）
            pre_node = bst.find_prev(A[i])
            even_jump[i] = pre_node[0] != -1 and odd_jump[pre_node[1]]
            # 把cur加入当前bst
            bst.put(A[i], i)
        result = 0
        # 看每个起点的odd跳的结果
        for i in range(0, n):
            if odd_jump[i]:
                result += 1
        return result



class SortedArray:
    def __init__(self):
        self.array = []

    def put(self, val, index):
        i = 0
        while i < len(self.array):
            if val <= self.array[i][0]:
                break
            i += 1
        self.array.insert(i, [val, index])

    def find_prev(self, val):
        i = 0
        while i < len(self.array):
            if val <= self.array[i][0]:
                if val == self.array[i][0]:
                    return self.array[i]
                i -= 1
                break
            i += 1
        if i == len(self.array):
            i -= 1
        if i < 0:
            return [-1, -1]
        while i > 0:
            if self.array[i][0] != self.array[i-1][0]:
                break
            i -= 1
        return self.array[i]

    def find_next(self, val):
        i = 0
        while i < len(self.array):
            if val <= self.array[i][0]:
                if val == self.array[i][0]:
                    return self.array[i]
                break
            i += 1

        if i > len(self.array) - 1:
            return -1, -1
        return self.array[i]


############
import bisect
class Solution0:
    def oddEvenJumps(self, A):
        n = len(A)
        odd_jump = [False] * n
        even_jump = [False] * n
        bst = []
        # base case
        odd_jump[n - 1] = True
        even_jump[n - 1] = True
        bisect.insort_right(bst, A[n - 1])
        # general case
        for i in range(n - 2, -1, -1):
            # odd跳的结果 （比它大的里面找最小的）
            next_node = bisect.bisect_right(bst, A[i])
            odd_jump[i] = next_node != len(bst) and even_jump[next_node]
            # even跳的结果（比它小的里面找最大的）
            pre_node = bisect.bisect_left(bst, A[i])
            even_jump[i] = pre_node != 0 and odd_jump[pre_node]
            # 把cur加入当前bst
            bisect.insort_left(bst, A[i])
        result = 0
        # 看每个起点的odd跳的结果
        for i in range(0, n):
            if odd_jump[i]:
                result += 1
        return result
s = Solution0()
a = [2,3,1,1,4] # 3
print(s.oddEvenJumps(a))
a = [10,13,12,14,15] # 2
print(s.oddEvenJumps(a))
a = [5,1,3,4,2] # 3
print(s.oddEvenJumps(a))
a = [1,2,3,2,1,4,4,5] # 6
print(s.oddEvenJumps(a))
a = [5,1,3,4,2] #3
print(s.oddEvenJumps(a))




