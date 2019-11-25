class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        res = []
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            res.append('-')
        dividend = abs(numerator)
        divisor = abs(denominator)
        res.append(str(dividend // divisor))
        remainder = dividend % divisor
        if remainder == 0:
            return ''.join(res)
        res.append('.')
        remainder_hash = {}
        while remainder != 0:
            if remainder in remainder_hash:
                res.insert(remainder_hash[remainder], '(')
                res.append(')')
            remainder_hash[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // divisor))
            remainder %= divisor
        return ''.join(res)

s = Solution()
a = 1
b = 2
print(s.fractionToDecimal(a, b))
