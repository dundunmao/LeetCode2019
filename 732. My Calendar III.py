import collections


class MyCalendarThree:

    def __init__(self):
        self.range = {}

    def book(self, start: int, end: int) -> int:
        self.range[start] = self.range[start] + 1 if start in self.range else 1
        self.range[end] = self.range[end] - 1 if end in self.range else -1
        active = 0
        ans = 0
        sort_time = sorted(self.range.keys())
        for time in sort_time:
            active += self.range[time]
            ans = max(ans, active)
        return ans

# Your MyCalendarThree object will be instantiated and called as such:
obj = MyCalendarThree()
a = [[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
for ele in a:
    print(obj.book(ele[0],ele[1]))
