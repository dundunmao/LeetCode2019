

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        start = 1
        end = x
        while start+1 < end:
            mid = start+(end-start)/2
            if mid*mid <= x:
                start = mid
            else:
                end = mid
        if end*end <=x:
            return end
        return start

    def mySqrt_leet(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
            return 0
        if x == 1:
            return 1
        start = 1
        end = x
        while start + 1 < end:
            mid = (start+end)/2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                start = mid
            else:
                end = mid
        return start
    
class SolutionNew:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        s = 0
        e = x //2
        while s + 1 < e:
            m = s + (e - s) // 2
            if m*m == x:
                return m
            elif m*m < x:
                s = m
            else:
                e = m
        if e * e <= x:
            return e
        else:
            return s
        
if __name__ == "__main__":
    x = 10
    s = Solution()
    print s.sqrt(x)
