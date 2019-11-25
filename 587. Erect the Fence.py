class Solution:
    def outerTrees(self, points):
        point_array = []
        for p in points:
            point = Point(p[0], p[1])
            point_array.append(point)
        point_array.sort()
        point_stack = []

        for i in range(len(point_array)):
            while len(point_stack) >= 2 and self.orientation(point_stack[-2], point_stack[-1], point_array[i]) > 0:
                point_stack.pop()
            point_stack.append(point_array[i])

        for i in range(len(point_array) - 1, -1, -1):
            while len(point_stack) >= 2 and self.orientation(point_stack[-2], point_stack[-1], point_array[i]) > 0:
                point_stack.pop()
            point_stack.append(point_array[i])
        res = set()
        for ele in point_stack:
            res.add((ele.x, ele.y))
        return res

    def orientation(self, p, q, r):
        return (q.y - p.y) * (r.x - p.x) - (q.x - p.x) * (r.y - p.y)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(a, b):  # 按x的从小到大排，如果相等，按y的从大到小
        if a.x == b.x:
            return b.y < a.y
        return a.x < b.x
    
x = Solution()
p = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
print(x.outerTrees(p))
