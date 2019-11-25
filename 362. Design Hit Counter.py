from collections import deque


class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.count = 0

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        while len(self.q) != 0 and timestamp - self.q[0] >= 300:
            self.q.popleft()
            self.count -= 1
        self.q.append(timestamp)
        self.count += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while len(self.q) != 0 and timestamp - self.q[0] >= 300:
            self.q.popleft()
            self.count -= 1
        return self.count



        # Your HitCounter object will be instantiated and called as such:
        # obj = HitCounter()
        # obj.hit(timestamp)
        # param_2 = obj.getHits(timestamp)