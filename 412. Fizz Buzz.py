class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        for i in range(1,n+1):
            if i%5==0 and i%3 == 0:
                res.append("FizzBuzz")
            elif i%3 == 0:
                res.append("Fizz")
            elif i%5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res

if __name__ == "__main__":
    s = 15
    x = Solution()
    print x.fizzBuzz(s)