# dp

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        n, m = len(S), len(T)
        f = [0] * (m + 1)
        first_index = -1
        dist = -1
        for i in range(n, -1, -1):
            for j in range(0, m + 1):
                if i == n and j == m:
                    f[j] = 0
                elif i == n:
                    f[j] = -1
                elif j == m:
                    f[j] = 0
                else:
                    if S[i] == T[j]:
                        if f[j + 1] == -1:
                            f[j] = -1
                        else:
                            f[j] = 1 + f[j + 1]
                    else:
                        if f[j] == -1:
                            f[j] = -1
                        else:
                            f[j] = 1 + f[j]
            if f[0] != -1 and (first_index == -1 or f[0] <= dist):
                first_index = i
                dist = f[0]
        return '' if first_index == -1 else S[first_index: first_index + dist]


# two pointer

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        start_index = -1
        dist = -1
        n = len(S)
        m = len(T)

        for i in range(n):
            if S[i] == T[0]:
                cur_dist = self.compare(S, i, T)
                if cur_dist != -1 and (dist == -1 or cur_dist < dist):
                    start_index = i
                    dist = cur_dist
        return '' if start_index == -1 else S[start_index: start_index + dist]

    def compare(self, a, start, b):
        i = start
        j = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j == len(b):
            return i - start
        else:
            return -1
