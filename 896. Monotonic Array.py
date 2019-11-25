class Solution1:
    def isMonotonic(self, A) -> bool:
        increase = True
        i = 1
        # 先找是升序还是降序
        while i < len(A):
            if A[i - 1] > A[i]:
                increase = False
                break
            elif A[i - 1] < A[i]:
                break
            i += 1
        # 根据升或降来查
        if increase == True:
            while i < len(A):
                if A[i - 1] > A[i]:
                    return False
                i += 1
        else:
            while i < len(A):
                if A[i - 1] < A[i]:
                    return False
                i += 1
        return True
class Solution:
    def isMonotonic(self, a) -> bool:
        increase = False
        decrease = False
        for i in range(1, len(a)):
            if a[i - 1] > a[i]:
                decrease = True
            elif a[i - 1] < a[i]:
                increase = True
        if increase and decrease:
            return False
        else:
            return True
s = Solution()
a = [1,2,2,3]
print(s.isMonotonic(a))
