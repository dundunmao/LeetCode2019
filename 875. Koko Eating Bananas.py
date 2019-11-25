class Solution:
    def minEatingSpeed(self, piles, H):
        start = 1
        end = max(piles)
        while start + 1 < end:
            mid = start + (end - start) // 2
            hours = self.need_hours(piles, mid)
            if hours <= H:
                end = mid
            else:
                start = mid

        start_hour = self.need_hours(piles, start)
        end_hour = self.need_hours(piles, end)
        if start_hour <= H:
            return start
        elif end_hour <= H:
            return end
    # 给一个speed，算出吃完需要多少个小时
    def need_hours(self, piles, speed):
        res = 0
        for ele in piles:
            if ele % speed == 0:
                res += ele // speed
            else:
                res += ele // speed + 1
        return res
s = Solution()
# a = [3,6,7,11]
# b = 8
# print(s.minEatingSpeed(a,b)) #4
a = [30,11,23,4,20]
b = 23
print(s.minEatingSpeed(a,b)) #4
