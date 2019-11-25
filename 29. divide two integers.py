
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor or dividend == 0:
            return 0
        res = self.helper(dividend, divisor)
        ans = sign * res
        if ans > 2147483647:
            return 2147483647
        else:
            return ans

    def helper(self, dividend, divisor):
        if dividend < divisor:
            return 0
        sum = divisor
        multiple = 1
        while sum + sum <= dividend:
            sum += sum
            multiple += multiple
        return multiple + self.helper(dividend - sum, divisor)

class Solution:
    # 答案
    def divide(self, dividend, divisor):
        # write your code here
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
            neg = True
        else:
            neg = False
        a = abs(dividend)
        b = abs(divisor)
        ans = 0
        shift = 31
        while shift >= 0:
            if a >= (b << shift):  # 9<<3（左移3位）相当于9 * 2^3=9*8=72
                a -= (b << shift)
                ans += (1 << shift)  #1<<1（左移1位）相当于1 * 2^1=2
            shift -= 1
        if neg:
            ans = - ans
        if ans > INT_MAX:
            return INT_MAX
        return ans


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor or dividend == 0:
            return 0
        res = 0
        left = dividend
        base = divisor
        while left >= base:
            time, left = self.helper(base, left)
            res += time
        res = res * sign
        if res >= 2147483647:
            return 2147483647
        return res


    def helper(self, base, left):
        time = 1
        if base * (time + time) <= left:
            while left >= base * (time + time):
                time += time
            left -= base * (time)
            return time, left
        else:
            return time, left - base

if __name__ == "__main__":
    a = 100
    b = 9
    s = Solution()
    # print s.helper(b)
    print s.divide(a,b)
