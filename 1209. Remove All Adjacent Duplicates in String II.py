class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        # for i in range(len(s)):
        for ele in s:
            if len(stack) > 0:
                if stack[-1][0] == ele:
                    temp, num = stack.pop()
                    if num < k - 1:
                        stack.append([temp, num + 1])
                else:
                    stack.append([ele, 1])
            else:
                stack.append([ele, 1])
        res = ''
        for temp, num in stack:
            for i in range(num):
                res += temp
        return res
