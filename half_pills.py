# DFS
class Solution:
    def half_pills(self, n, k):
        all_result = {}
        return self.dfs(0, k, n, 0, all_result)

    def dfs(self, current, k, full, half, all_result):
        key = str(full) + '#' + str(half)
        if key in all_result:
            return all_result[key]
        total = full + half
        if current == k:
            return half / total
        res = 0
        if full > 0:
            res += (full / total) * self.dfs(current + 1, k, full - 1, half + 1, all_result)
        if half > 0:
            res += (half / total) * self.dfs(current + 1, k, full, half - 1, all_result)
        all_result[key] = res
        return res

# DP
class Solution1:

    def half_pills(self, n, k):
        # all_result[i][j]表示第i天有j个full时的结果
        all_result = [[0.0 for i in range(n + 1)] for j in range(k + 1)]
        for i in range(k, -1, -1):
            for j in range(n, -1, -1):
                full = j
                day = i
                half = (n - full) * 2 - day
                total = full + half
                if all_result[i][j] != 0.0:
                    continue
                if total == 0 or half < 0 :
                    continue
                elif day == k:
                    all_result[i][j] = half / total
                else:
                    if full != 0:
                        all_result[i][j] += full / total * all_result[i + 1][j - 1]
                    if half != 0:
                        all_result[i][j] += half / total * all_result[i + 1][j]
        return all_result[0][n]

s = Solution()
n = 3
k = 3
print(s.half_pills(n, k)) #0.61

n = 2
k = 2
print(s.half_pills(n, k)) # 0.5
n = 100
k = 99
print(s.half_pills(n, k)) # 0.5321961583405944
