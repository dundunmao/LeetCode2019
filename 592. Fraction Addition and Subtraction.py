class Solution:
    def fractionAddition(self, expression: str) -> str:
        res = FracNum(0, 1)
        start = 0
        numerator = 0
        denominator = 1
        for i in range(1, len(expression)):
            if expression[i] == '/':
                numerator = int(expression[start : i])
                start = i + 1
            if expression[i] == '+' or expression[i] == '-':
                denominator = int(expression[start : i])
                cur = FracNum(numerator, denominator)
                res.add(cur)
                start = i
        denominator = int(expression[start:])
        last = FracNum(numerator, denominator)
        res.add(last)
        return str(res.numerator) + '/' + str(res.denominator)

class FracNum:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, cur):
        self.numerator = self.numerator * cur.denominator + self.denominator * cur.numerator
        self.denominator = self.denominator * cur.denominator
        gcd = self.gcd(abs(self.numerator), self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)
s = Solution()
a = "-1/2+1/2"
print((s.fractionAddition(a))) #"0/1"
a = "1/3-1/2"
print((s.fractionAddition(a))) #"-1/6"
a = "-1/2+1/2+1/3"
print((s.fractionAddition(a))) #"1/3"
