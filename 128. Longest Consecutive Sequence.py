# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.
# 麻烦的做法
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_to_count_set = set(nums)

        node_list = {}
        for value in num_to_count_set:
            if value + 1 in num_to_count_set:
                if value in node_list:
                    node_small = node_list[value]
                else:
                    node_small = Node(value)
                    node_list[value] = node_small

                if value + 1 in node_list:
                    node_big = node_list[value + 1]
                else:
                    node_big = Node(value + 1)
                    node_list[value + 1] = node_big
                node_small.next = node_big
                node_big.pre = node_small
        head_list = []
        for node in node_list.values():
            if node.pre == None:
                head_list.append(node)
        res = 1
        for node in head_list:
            length = 1
            while node.next:
                length += 1
                node = node.next
            res = max(res, length)
        return res


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None
##########################

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        maxlen = 0
        while nums:
            first = last = nums.pop()
            while first - 1 in nums:
                first -= 1
                nums.remove(first)
            while last + 1 in nums:
                last += 1
                nums.remove(last)
            maxlen = max(maxlen, last - first + 1)
        return maxlen

