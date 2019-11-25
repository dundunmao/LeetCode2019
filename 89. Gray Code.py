class Solution1(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(0,1<<n):
            res.append(i^i>>1)
        return res
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        res = [0]
        temp = []
        for i in range(0,n):
            le = len(res)
            for k in range(le-1,-1,-1):
                res.append(res[k] | 1 << i)   #res里有i个元素时，1就左移i-1位
                temp.append(bin(res[k] | 1 << i))
        return res


if __name__ == "__main__":
    nums = 4
    x = Solution()

    print x.grayCode(nums)
