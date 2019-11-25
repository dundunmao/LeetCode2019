class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.i = 0
        self.j = 0
        self.k = 0
        self.v1 = v1
        self.v2 = v2
        if len(self.v1) == 0:
            self.k = 1

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            if self.k == 0:
                return_value =self.v1[self.i]
                if self.j < len(self.v2):
                    self.k = 1
                self.i += 1
            else:
                return_value =self.v2[self.j]
                if self.i < len(self.v1):
                    self.k = 0
                self.j += 1
            return return_value
        else:
            return None

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.k == 0:
            if self.i < len(self.v1):
                return True
            else:
                return False
        else:
            if self.j < len(self.v2):
                return True
            else:
                return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
