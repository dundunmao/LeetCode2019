class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.row = 0
        self.col = 0
        self.a = v
        # 如果下一个row是空的，往下走一个
        while self.row < len(self.a) and len(self.a[self.row]) == 0:
            self.row += 1

    def next(self) -> int:

        t = self.a[self.row][self.col]
        self.update_next_index()
        return t

    def hasNext(self) -> bool:
        if self.row < len(self.a) and self.col < len(self.a[self.row]):
            return True
        else:
            return False

    def update_next_index(self):
        # 当行没到底，就后走
        if self.col + 1 < len(self.a[self.row]):
            self.col += 1
        else:
            # 当行到底了，就到下一行，并且把空行让出去
            self.row += 1
            self.col = 0
            while self.row < len(self.a) and len(self.a[self.row]) == 0:
                self.row += 1

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
