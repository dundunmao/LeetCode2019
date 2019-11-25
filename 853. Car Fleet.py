class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        car_stack = []
        for p, s in zip(position, speed):
            car_stack.append(Car(p, s))
        if not car_stack:
            return 0
        car_stack.sort()
        res = 1
        car = car_stack.pop()
        time_to_go = (target - car.pos) / car.speed
        while len(car_stack):
            car = car_stack.pop()
            if (target - car.pos) / car.speed > time_to_go:
                res += 1
                time_to_go = (target - car.pos) / car.speed
        return res


class Car():
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed

    def __lt__(a, b):
        return a.pos < b.pos

s = Solution()
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(s.carFleet(target, position, speed))
target = 10
position = [6,8]
speed = [3,2]
print(s.carFleet(target, position, speed))
