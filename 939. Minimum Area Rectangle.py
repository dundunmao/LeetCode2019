class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        row = {}
        # 按row为key,val为对应的col的set,建map
        for x, y in points:
            if x in row:
                row[x].add(y)
            else:
                row[x] = set()
                row[x].add(y)

        res = float('inf')
        n = len(points)
        # 每次确定A,B 两个点，然后去找 C,D
        # 然后看C，D在不在map里，在，就可以算一次答案
        for i in range(n):
            for j in range(i + 1, n):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]

                if x1 == x2 or y1 == y2:
                    continue

                x3 = x2
                y3 = y1
                x4 = x1
                y4 = y2

                if y3 not in row[x3]:
                    continue
                if y4 not in row[x4]:
                    continue
                res = min(res, abs(x2 - x1) * abs(y1 - y2))

        return 0 if res == float('inf') else res
