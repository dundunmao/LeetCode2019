class Solution(object):
    def numFriendRequests(self, ages):
        count = [0] * 121
        for age in ages:
            count[age] += 1
        ans = 0
        for ageA, countA in enumerate(count):
            if countA == 0:
                continue
            for ageB, countB in enumerate(count):
                if countB == 0:
                    continue
                if self.check(ageA, ageB):
                    ans += countA * countB
                    if ageA == ageB:
                        ans -= countA
        return ans

    def check(self, ageA, ageB):
        if ageA * 0.5 + 7 >= ageB:
            return False
        if ageA < ageB:
            return False
        if ageA < 100 < ageB:
            return False
        return True
s = Solution()
a = [20,30,100,110,120]
print(s.numFriendRequests(a))
