class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []
        while i < len(A) and j < len(B):
            if A[i][0] <= B[j][0]:
                if A[i][1] < B[j][0]:
                    i += 1
                elif A[i][1] <= B[j][1]:
                    res.append([B[j][0], A[i][1]])
                    i += 1
                else:
                    res.append([B[j][0], B[j][1]])
                    j += 1
            else:
                if A[i][0] > B[j][1]:
                    j += 1
                elif A[i][1] >= B[j][1]:
                    res.append([A[i][0], B[j][1]])
                    j += 1
                else:
                    res.append([A[i][0], A[i][1]])
                    i += 1
        return res
