class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        capacity_array = []
        for trip in trips:
            capacity_array.append(SeatCapacity(trip[0], trip[1], 1))
            capacity_array.append(SeatCapacity(trip[0], trip[2], -1))
        capacity_array.sort()
        res = 0
        seat = 0
        for seat_cap in capacity_array:
            if seat_cap.state == -1:
                seat -= seat_cap.num
            elif seat_cap.state == 1:
                seat += seat_cap.num
            res = max(res, seat)
        return res <= capacity


class SeatCapacity:
    def __init__(self, num, time, state):
        self.num = num
        self.time = time
        self.state = state

    def __le__(a, b):
        if a.time == b.time:
            return a.state < b.state
        return a.time < b.time

s = Solution()
a = [[2,1,5],[3,3,7]]
b = 4
print(s.carPooling(a, b))
