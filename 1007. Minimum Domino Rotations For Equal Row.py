class Solution:
    def minDominoRotations(self, A, B) -> int:
        res = []
        # not rotated the first
        res_1 = self.helper(A[0], A, B)
        if res_1 != -1:
            res.append(res_1)
        res_2 = self.helper(B[0], B, A)
        if res_2 != -1:
            res.append(res_2)
        # rotated the first
        res_3 = self.helper(A[0], B, A)
        if res_3 != -1:
            res.append(res_3 + 1)
        res_4 = self.helper(B[0], A, B)
        if res_4 != -1:
            res.append(res_4 + 1)

        if len(res) == 0:
            return -1
        else:
            return min(res)

    def helper(self, target, original, rotated):
        res = 0
        for i in range(1, len(original)):
            if original[i] != target and rotated[i] == target:
                res += 1
            elif original[i] != target and rotated[i] != target:
                res = -1
                break
        return res

s = Solution()
a =[2,1,2,4,2,2]
b =[5,2,6,2,3,2]
print(s.minDominoRotations(a, b)) # 2
a =[3,5,1,2,3]
b =[3,6,3,3,4]
print(s.minDominoRotations(a, b)) # -1
a = [1, 2, 1, 3]
b = [1, 1, 2, 1]
print(s.minDominoRotations(a, b)) # 1
