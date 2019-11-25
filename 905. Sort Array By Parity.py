class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        le = 0
        size = len(A)
        for i in range(0, size):
            if A[i] % 2 == 0:
                A[i], A[le] = A[le], A[i]
                le += 1
        return A
