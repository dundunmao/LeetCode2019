import bisect
import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        # number of points in each rectangle
        self.counts = [(x2 - x1 + 1) * (y2 - y1 + 1)
                       for x1, y1, x2, y2 in rects]
        self.total = sum(self.counts)
        # accumulated (prefix) count of points
        self.accumulate_counts = []
        accumulated = 0
        for count in self.counts:
            accumulated += count
            self.accumulate_counts.append(accumulated)

    def pick(self) -> List[int]:
        rand = random.randint(1, self.total)
        # bisect_left(a, num) 表示，a里如果有num,就返回num的index，如果没有，就返回他该插入的位置，这里就可以得到他属于第几块rectangle
        rect_index = bisect.bisect_left(self.accumulate_counts, rand)
        # 表示在找到的rectangle里是第几个点
        point_index = rand - self.accumulate_counts[rect_index] + self.counts[rect_index] - 1
        x1, y1, x2, y2 = self.rects[rect_index]
        # 用 mod去找在第几行和第几列
        row = point_index // (y2 - y1 + 1)
        col = point_index % (y2 - y1 + 1)
        return [x1 + row, y1 + col]
