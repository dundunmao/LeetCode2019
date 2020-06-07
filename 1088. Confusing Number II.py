import collections
class Solution:
    def confusingNumberII(self, N: int) -> int:
        base = [0, 1, 6, 8, 9]
        reversed_base = {0:0, 1:1, 6:9, 8:8, 9:6}
        t = N
        level = 0
        high_bit = 10
        while t > 0:
            t //= 10
            if t != 0:
                high_bit = t
            level += 1
        ans = 0
        if level == 10:
            N -= 1
            ans = 1
            level -= 1
        q = collections.deque()
        q.append(0)
        # ori = 0
        for i in range(level):
            size = len(q)
            while size > 0:
                base_i = q.popleft()
                for j in range(0, 5):
                    cur = base[j]
                    if i == 0 and cur == 0:
                        continue
                    if i == level - 1 and base_i > high_bit:
                        break
                    # build
                    ori = base_i * 10 + cur
                    if ori <= N:
                        # store
                        q.append(ori)
                        # reverse
                        rev = 0
                        res_ori = ori
                        while res_ori > 0:
                            rev = rev * 10 + reversed_base[res_ori % 10]
                            res_ori //= 10
                        # check
                        if rev != ori:
                            print(ori)
                            ans += 1
                size -= 1
        return ans


class Solution:
    def __init__(self):
        self.count = 0

    def confusingNumberII(self, N):

        valid = [0, 1, 6, 8, 9]
        mapping = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        self.dfs(1, 1, 10, valid, mapping, N)
        self.dfs(6, 9, 10, valid, mapping, N)
        self.dfs(8, 8, 10, valid, mapping, N)
        self.dfs(9, 6, 10, valid, mapping, N)

        return self.count

    def dfs(self, v, rotation, digit, valid, mapping, N):
        if v:
            if v != rotation:
                self.count += 1

        for i in valid:
            if v * 10 + i > N:
                break
            else:
                self.dfs(v * 10 + i, mapping[i] * digit + rotation, digit * 10, valid, mapping, N)


s = Solution1()
# a = 20
# print(s.confusingNumberII(a))
a = 1000000000
print(s.confusingNumberII(a))
