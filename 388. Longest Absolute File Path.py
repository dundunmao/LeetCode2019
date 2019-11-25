class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        stack.append(0)
        res = 0
        input_array = input.split('\n')
        for ele in input_array:
            level = ele.count('\t') + 1 #有几个t就是第几级
            while level + 1 < len(stack): #把stack里比我低的级都pop出去，
                stack.pop()
            size = stack[-1] + len(ele) - level + 1 # stack里存的是从头到我现在这个node一个都长
            stack.append(size)
            if '.' in ele: #如果当前的file了，就算一下长度
                res = max(res, size - 1)
        return res
s = Solution()
a = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(s.lengthLongestPath(a))
