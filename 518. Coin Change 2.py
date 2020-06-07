class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        f = [[0 for i in range(amount + 1)] for j in range(m + 1)]

        for i in range(0, m + 1):
            for j in range(0, amount + 1):
                if j == 0:
                    f[i][j] = 1
                elif i == 0:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i - 1][j]
                    if j - coins[i - 1] >= 0:
                        f[i][j] += f[i][j - coins[i - 1]]
        return f[m][amount]
    
s = Solution()
# a = 5
# c = [1, 2, 5]
# print(s.change(a, c))
a = 5
c = [2,5]
print(s.change(a, c))
