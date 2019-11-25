class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        if n <= 1:
            return A
        # 从后往前找一段升序，找到升序段前面那个位置，target
        i = n - 2
        while i >= 0 and A[i] <= A[i + 1]:
            i -= 1
        if i < 0:
            return A
        # 在升序段，，从后往前，找第一个小于target的数
        j = n - 1
        while j > i and A[j] >= A[i]:
            j -= 1
        # 找第一个出现这个数的位置
        while j - 1 >= 0 and A[j] == A[j - 1]:
            j -= 1
        # 交换
        A[i], A[j] = A[j], A[i]
        return A
