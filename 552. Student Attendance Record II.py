class Solution:
    def checkRecord(self, n: int) -> int:
        dp00 = [0] * (n + 1)
        dp01 = [0] * (n + 1)
        dp02 = [0] * (n + 1)
        dp10 = [0] * (n + 1)
        dp11 = [0] * (n + 1)
        dp12 = [0] * (n + 1)

        dp00[0] = 1
        M = 10 ** 9 + 7
        for i in range(1, n + 1):
            dp00[i] = (dp00[i - 1] + dp01[i - 1] + dp02[i - 1]) % M
            dp01[i] = dp00[i - 1]
            dp02[i] = dp01[i - 1]
            dp10[i] = (dp00[i - 1] + dp01[i - 1] + dp02[i - 1] + dp10[i - 1] + dp11[i - 1] + dp12[i - 1]) % M
            dp11[i] = dp10[i - 1]
            dp12[i] = dp11[i - 1]
        return (dp00[n] + dp01[n] + dp02[n] + dp10[n] + dp11[n] + dp12[n]) % M
