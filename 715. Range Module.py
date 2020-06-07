import bisect
class RangeModule:

    def __init__(self):
        self.track = []

    def addRange(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 0: #说明起点不在某个range里
            subtrack.append(left) #说明终点不在某个range里
        if end % 2 == 0:
            subtrack.append(right)

        self.track[start:end] = subtrack

    def removeRange(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)

        self.track[start:end] = subtrack

    def queryRange(self, left, right):
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)

        return start == end and start % 2 == 1

# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()

obj.addRange(10, 20)
obj.addRange(40, 50)
obj.addRange(15, 17)

obj.removeRange(14, 16)
obj.addRange(15, 17)
print(obj.queryRange(10, 14)) #T
print(obj.queryRange(13, 15)) #F
print(obj.queryRange(16, 17)) #T
obj.addRange(15, 17)
