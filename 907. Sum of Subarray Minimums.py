class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        stack.append([A[0], 0, A[0]])
        res = A[0]
        for i in range(1, len(A)):
            while len(stack) > 0 and stack[-1][0] >= A[i]:
                stack.pop()
            if len(stack) == 0:
                temp = A[i] * (i + 1)
            else:
                temp = A[i] * (i - stack[-1][1]) + stack[-1][2]
            stack.append([A[i], i, temp])
            # calculate
            res += temp
        return res % (10 ** 9 + 7)

# 带object的

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        node = Node(A[0], 0, A[0])
        stack.append(node)
        res = node.total_until_now
        for i in range(1, len(A)):
            while len(stack) > 0 and stack[-1].value >= A[i]:
                stack.pop()
            if len(stack) == 0:
                temp = A[i] * (i + 1)
            else:
                temp = A[i] * (i - stack[-1].index) + stack[-1].total_until_now
            node = Node(A[i], i, temp)
            stack.append(node)
            # calculate
            res += temp
        return res % (10 ** 9 + 7)


class Node:
    def __init__(self, value, index, total_until_now):
        self.value = value
        self.index = index
        self.total_until_now = total_until_now

# 超时的
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stack = []
        stack.append([A[0], 0])
        res = A[0]
        for i in range(1, len(A)):
            while len(stack) > 0 and stack[-1][0] >= A[i]:
                stack.pop()
            stack.append([A[i], i])
            # calculate
            res += self.sum_up(A, stack)
        return res % (10**9 + 7)
    def sum_up(self, A, stack):
        res = 0
        for i in range(len(stack) - 1, -1, -1):
            if i == 0:
                res += stack[i][0]*(stack[i][1] + 1)
            else:
                res += stack[i][0]*(stack[i][1] - stack[i - 1][1])
        return res
