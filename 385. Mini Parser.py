"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0].isdigit() or s[0] == '-':  # 第一个是正或负数
            return NestedInteger(int(s))
        nested_interger_stack = []
        # facke base case
        nested_interger_stack.append(NestedInteger())
        # general case
        start = 0
        for i in range(len(s)):
            c = s[i]
            if c == ',':
                # 如果','前面是数字
                if s[i - 1].isdigit():
                    # 生成一个integer的NestedInteger
                    nest_integer = NestedInteger(int(s[start: i]))
                    # 在生成一个list的NestedInteger， 把前面的interger放里面
                    nested_interger_stack[-1].getList().append(nest_integer)
                # start 走到 ',' 后面
                start = i + 1
            elif c == '[':
                # 遇到'【'就生成一个新的node
                nest_integer = NestedInteger()
                # 并加入stack里
                nested_interger_stack.append(nest_integer)
                # start 走到 '[' 后面
                start = i + 1
            elif c == ']':
                # 如果']'前面是数字
                if s[i - 1].isdigit():
                    # 生成一个integer的NestedInteger
                    nest_integer = NestedInteger(int(s[start: i]))
                    # 在生成一个list的NestedInteger， 把前面的interger放里面
                    nested_interger_stack[-1].getList().append(nest_integer)
                # 因为']'意味这一层结束了，可以pop出来，并且塞到上一个NestedInteger里面
                nest_integer = nested_interger_stack.pop()
                nested_interger_stack[-1].add(nest_integer)
        return nested_interger_stack[-1].getList()[0]



