class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        i = 0
        while i < len(dominoes):
            j = i + 1
            # case 1
            while j < len(dominoes) and dominoes[j] != 'R' and dominoes[j] != 'L':
                j += 1
            if j == len(dominoes):
                j -= 1
            if dominoes[i] != 'R' and dominoes[i] != 'L':
                if dominoes[j] == 'L':
                    for k in range(i, j + 1):
                        dominoes[k] = 'L'
            elif dominoes[i] == 'R':
                if dominoes[j] == 'L':
                    mid = (j + i) // 2
                    if (j - i) % 2 == 0:
                        for k in range(i + 1, mid):
                            dominoes[k] = 'R'
                        for k in range(mid + 1, j):
                            dominoes[k] = 'L'
                    else:
                        for k in range(i + 1, mid + 1):
                            dominoes[k] = 'R'
                        for k in range(mid + 1, j):
                            dominoes[k] = 'L'
                        # 都对倒
                else:
                    for k in range(i , j + 1):
                        dominoes[k] = 'R'
                    # 全倒向R
            else:
                if dominoes[j] == 'L':
                    # 全倒向L
                    for k in range(i + 1, j):
                        dominoes[k] = 'L'
                # else do nothing
            if j == len(dominoes) - 1:
                break
            i = j
        return ''.join(dominoes)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        domi_char = list(dominoes)
        start = 0 if domi_char[0] == '.' else 1
        for i in range(1, n):
            if domi_char[i] != '.': #找右墙
                if domi_char[i - 1] == '.':
                    self.process(start, i, domi_char) #start是这一段的第一个'.'，start-1是左墙
                start = i + 1
        if domi_char[n - 1] == '.':
            self.process(start, n, domi_char)
        return ''.join(domi_char)
    def process(self, start, end, domi_char):
        start_op = 'L' if start == 0 else domi_char[start - 1]
        end_op = 'R' if end == len(domi_char) else domi_char[end]
        if start_op == end_op: #如果两个墙是同方向，中间的'.'都是同方向
            for i in range(start, end):
                domi_char[i] = start_op
        if start_op == 'R' and end_op == 'L': #如果是一右一左，中间的点往中间倒，
            end -= 1
            while start < end:
                domi_char[start] = 'R'
                domi_char[end] = 'L'
                start += 1
                end -= 1



s = Solution()
a = ".L.R...LR..L.." #"LL.RR.LLRRLL.."
print(s.pushDominoes(a))
b = "RR.L"
print(s.pushDominoes(b)) # "RR.L"
b = ".L.R."
print(s.pushDominoes(b)) # "LL.RR"
