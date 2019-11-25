class RLEIterator:

    def __init__(self, A):
        self.A = A
        self.pointer = 1  # 当前char的位置
        self.num = 0  # 当前已经用掉几个

    def next(self, n):
        while self.pointer < len(self.A):
            # 当前char剩下不到n个了
            if n > self.A[self.pointer - 1] - self.num:
                # n把当前这个char还有的数都用掉，再去下一个
                n -= self.A[self.pointer - 1] - self.num
                self.num = 0
                self.pointer += 2
            # 当前char剩下的比n个大，就返回这个char
            else:
                self.num += n  # 当前又消耗掉n个
                return self.A[self.pointer]
        return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
