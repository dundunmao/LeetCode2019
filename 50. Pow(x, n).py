
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0 or x == 1:  #处理 0^n和1^n
            return 1
        if n == 1:   #处理 x^1
            return x
        if n < 0:    #处理 x^(-n)
            # return 1 / self.myPow(x, -n)  本来可以这样。但因当n=Integer.MIN_VALUE会出问题
            # Integer.MAX_VALUE =  2147483647
            # Integer.MIN_VALUE = -2147483648
            # 差一个数，下面就是处理这个东西
            return 1/(x*self.myPow(x,-(n+1)))
        res = 1
        while n > 1:
            if n % 2 == 1: #如果power是奇数
                res *= x  #把结果先自乘一个x
            x = x*x    #底数翻倍
            n /= 2      #power 除2
        res *= x
        return res
