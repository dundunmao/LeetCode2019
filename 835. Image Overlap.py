class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        res = 0
        a_array = []
        b_array = []
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    a_array.append((i, j))
                if B[i][j] == 1:
                    b_array.append((i, j))
        b_set = set(b_array)
        seen = set()
        for a in a_array:
            for b in b_array:
                delta = (b[0] - a[0], b[1] - a[1]) #记录移动步骤
                if delta not in seen:
                    seen.add(delta)
                    temp_result = 0
                    for point in a_array:
                        if (point[0] + delta[0], point[1] + delta[1]) in b_set:
                            temp_result += 1
                    res = max(res, temp_result)
        return res

s = Solution()
# A = [[1,1,0],[0,1,0],[0,1,0]]
# B = [[0,0,0], [0,1,1],[0,0,1]]
# print((s.largestOverlap(A, B))) # 3

A = [[0,1],[1,1]]
B = [[1,1],[1,1]]
print((s.largestOverlap(A, B))) # 3
