# Given a nested list of integers, implement an iterator to flatten it.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Example 1:
# Given the list [[1,1],2,[1,1]],
#
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
#
# Example 2:
# Given the list [1,[4,[6]]],
#
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].


class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
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


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self):
        """
        :rtype: int
        """
        num = self.stack[-1].getInteger()
        self.stack.pop()
        return num

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack and not self.stack[-1].isInteger():
            data = self.stack[-1].getList()
            self.stack.pop()
            for i in range(len(data) - 1, -1, -1):
                self.stack.append(data[i])
        return len(self.stack) > 0


if __name__ == '__main__':


    nestedList = [[1,1],2,[1,1],2]
    nestedList = NestedInteger()
    i, v = NestedIterator(nestedList), []
    while i.hasNext():
        v.append(i.next())
