class Solution:
    def pancakeSort(self, A):
        res = []
        n = len(A)
        target = n
        for i in range(n):
            index = self.find_max(A, target)
            # if n - i == 2:
            #     self.revserse(A, index)
            #     res.append(index + 1)
            #     break
            self.revserse(A, index)
            self.revserse(A, target - 1)
            res.append(index + 1)
            res.append(target)
            target -= 1
        return res

    def find_max(self, A, target):
        for i in range(len(A)):
            if A[i] == target:
                return i
        return -1
    def revserse(self, A, i):
        s = 0
        e = i
        while s < e:
            A[s], A[e] = A[e], A[s]
            s += 1
            e -= 1
s = Solution()
a = [3,2,4,1]
print(s.pancakeSort(a))
