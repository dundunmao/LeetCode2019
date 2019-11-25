
class Solution(object):
    def firstMissingPositive(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(A):
            if A[i] == i+1 or A[i] <= 0 or A[i] > len(A):
                i+=1
            elif A[A[i]-1] != A[i]:
                self.swap(A,i,A[i]-1)
            else:
                i+=1
        i = 0
        while i < len(A) and A[i] == i+1:
            i += 1
        return i+1
    def swap(self,A,i,j):
        A[i],A[j] = A[j],A[i]
        return A
if __name__ == "__main__":
    a = [3,4,-1,1]
    x = Solution()
    print(x.firstMissingPositive(a))
    a = [7,8,9,11,12]
    print(x.firstMissingPositive(a))
