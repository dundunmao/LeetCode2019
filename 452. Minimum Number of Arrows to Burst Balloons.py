class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # sort by x_end
        points.sort(key=lambda x: x[1])
        res = 1
        n = len(points)
        arraw = points[0][1]
        for i in range(1, n):
            if points[i][0] > arraw:
                res += 1
                arraw = points[i][1]
        return res
