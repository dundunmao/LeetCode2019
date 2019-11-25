# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        new = sorted(intervals,key = lambda x: x.start)
        i = 0
        while i < len(new):
            j = i+1
            while j < len(new) and new[i].end >= new[j].start:
                new[i].end = max(new[i].end,new[j].end)
                del new[j]
            i += 1
        return new


class Solution1:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # 如果没重叠，就直接append.
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
            # 重叠了，就改一下res里最后一个interval的end
                res[-1][1] = max(res[-1][1], interval[1])

        return res

if __name__ == "__main__":
    a = []
    array = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # array = [[1, 4], [4, 5]]
    # for i in range(len(array)):
    #     x = Interval(array[i][0],array[i][1])
    #     a.append(x)


    s = Solution1()
    print(s.merge(array))
