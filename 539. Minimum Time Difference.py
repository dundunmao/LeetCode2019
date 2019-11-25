class Solution:
    def findMinDifference(self, timePoints):
        time_points = sorted([ele.split(':') for ele in timePoints], key=lambda x: (x[0],x[1]))
        mini = float('inf')
        n = len(time_points)
        for i in range(0, n - 1):
            mini = min(mini, self.calculate_diff(time_points[i], time_points[i + 1]))
        mini = min(mini, self.calculate_diff(time_points[0], time_points[n - 1])) #最后还要把头和尾也算一下diff
        return mini

    # 正着算一下，反着算一下，如果是负数，就用24*60减一下
    def calculate_diff(self, first, second):
        hours = int(second[0]) - int(first[0])
        minute = int(second[1]) - int(first[1])
        res = hours * 60 + minute
        res_reverse = 24 * 60 - hours * 60 - minute
        return min(res, res_reverse)



s = Solution()
# a = ["23:59", "00:00"]
# print(s.findMinDifference(a))
a = ["13:59", "01:01", "23:59","00:00"]
print(s.findMinDifference(a))
