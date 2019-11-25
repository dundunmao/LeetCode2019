class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:  # x = 9
            return 0
        if x < 0:  # x为负
            flag = True
            x = abs(x)
        else:
            flag = False
        res = []
        while x % 10 == 0:  # x 尾数有0
            x /= 10
        while x / 10 != 0:  # 从后往前，存入res这个array里
            res.append(x % 10)
            x /= 10
        res.append(x % 10)
        ans = 0
        for i in range(len(res)):  #for一遍组合起来
            ans += res[i] * 10 ** (len(res) - 1 - i)
        if ans > 2 ** 31:
            return 0
        if flag == True:
            return -ans
        return ans


class Solution1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:  # x = 9
            return 0
        if x < 0:  # x为负
            flag = True
            x = abs(x)
        else:
            flag = False
        res = []
        ans = 0
        while x % 10 == 0:  # x 尾数有0
            x /= 10
        while x / 10 != 0:  # 翻转
            ans = ans * 10 + (x % 10)
            x /= 10
        ans = ans * 10 + (x % 10)
        if ans > 2 ** 31:
            return 0
        if flag == True:
            return -ans
        return ans
if __name__ == "__main__":
    x = Solution1()

    print x.reverse(12300)
