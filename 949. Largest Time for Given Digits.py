class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = -1
        permu = self.permute(A)

        for h1, h2, m1, m2 in permu:
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""

    def permute(self, a):
        res = []
        path = []
        self.dfs(a, 0, res, path)
        return res

    def dfs(self, a, start, res, path):
        if start == len(a):
            res.append(path[:])
        else:
            for i in range(start, len(a)):
                a[i], a[start] = a[start], a[i]
                path.append(a[start])
                self.dfs(a, start + 1, res, path)
                path.pop()
                a[i], a[start] = a[start], a[i]
