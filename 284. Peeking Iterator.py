# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iters = iterator
        self.cur = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.cur is None:
            self.cur = self.next()
        return self.cur

    def next(self):
        """
        :rtype: int
        """
        if self.cur is not None:
            t = self.cur
            self.cur = None
            return t
        else:
            return self.iters.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur is not None:
            return True
        else:
            if self.iters.hasNext():
                self.cur = self.iters.next()
                return True
            else:
                return False

# Your PeekingIterator object will be instantiated and called as such:
nums = [1,2,3]
iter = PeekingIterator(Iterator(nums))
while iter.hasNext():
    val = iter.peek()   # Get the next element but not advance the iterator.
    iter.next()         # Should return the same value as [val].
