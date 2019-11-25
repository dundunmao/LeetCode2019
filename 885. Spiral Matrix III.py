class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int):
        r = r0
        c = c0
        count = 1
        step = 0
        res = [(r0, c0)]
        j = 0
        direction = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 右，下，左，上
        # 在结果里的node不能超过matrix的node
        while count < R * C:
            # k表示往前延伸几格，step是用来算k的取值范围的，j用来调方向
            for k in range(0, step // 2 + 1):
                r += direction[j][0]
                c += direction[j][1]
                # 如果没越界，就加入结果里
                if 0 <= r < R and 0 <= c < C:
                    res.append((r, c))
                    count += 1
            step += 1
            j = (j + 1) % 4
        return res
s = Solution()

print(s.spiralMatrixIII(R = 5, C = 6, r0 = 1, c0 = 4))
