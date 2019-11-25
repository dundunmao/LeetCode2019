# 开始的思路，是错的
class Solution:
    def asteroidCollision(self, asteroids):
        res_stack = []
        res_stack.append(asteroids[0])
        i = 1
        while i < len(asteroids):
            if len(res_stack) > 0:
                if res_stack[-1] > 0 and asteroids[i] < 0:
                    if abs(res_stack[-1]) > abs(asteroids[i]):
                        i += 1
                    elif abs(res_stack[-1]) == abs(asteroids[i]):
                        res_stack.pop()
                        i += 1
                    else:
                        while len(res_stack) > 0 and abs(res_stack[-1]) < abs(asteroids[i]):
                            res_stack.pop()
                        if len(res_stack) > 0 and abs(res_stack[-1]) == abs(asteroids[i]):
                            res_stack.pop()
                            i += 1
                        elif len(res_stack) == 0:
                            res_stack.append(asteroids[i])
                            i += 1
                        elif len(res_stack) > 0 and abs(res_stack[-1]) > abs(asteroids[i]):
                            i += 1
                else:
                    res_stack.append(asteroids[i])
                    i += 1
            else:
                res_stack.append(asteroids[i])
                i += 1

        return res_stack



class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res_stack = []
        for ele in asteroids:
            while len(res_stack) > 0 and res_stack[-1] > 0 and ele < 0 :
                if res_stack[-1] < -ele:
                    res_stack.pop()
                    continue
                elif res_stack[-1] == -ele:
                    res_stack.pop()
                break
            else:
                res_stack.append(ele)
        return res_stack


s = Solution()
# a = [5,10,-5]
# print(s.asteroidCollision(a))
# a = [8, -8]
# print(s.asteroidCollision(a))
a = [10, 2, -5]
print(s.asteroidCollision(a))

a = [-2, -1, 1, 2]
print(s.asteroidCollision(a))
