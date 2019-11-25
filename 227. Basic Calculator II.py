class Solution:
    def calculate(self, s: str) -> int:
        if s == '' or len(s) == 0:
            return 0
        res = []
        # res = 0
        sign = '+'
        num = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                num = int(s[start: i])
                i -= 1
            if s[i] in ['*', '-', '+', '/'] or i == len(s) - 1:
                if sign == '+':
                    res.append(num)
                elif sign == '-':
                    res.append(0 - num)
                elif sign == '*':
                    temp = res.pop()
                    res.append(temp * num)
                elif sign == '/':
                    temp = res.pop()
                    if temp * num > 0:
                        res.append(temp // num)
                    else:
                        res.append(-(abs(temp) // abs(num)))
                sign = s[i]
                num = 0
            i += 1
        return sum(res)


class Solution1:
    def calculate(self, s: str) -> int:
        if s == '' or len(s) == 0:
            return 0
        res = []
        n = len(s)
        sign = '+'
        num = 0
        i = 0
        while i < n:
            if s[i].isdigit():
                start = i
                while i < n and s[i].isdigit():
                    i += 1
                num = int(s[start:i])
                i -= 1
            if s[i] in ['+', '-', '*', '/'] or i == n - 1:
                if sign == '+':
                    res.append(num)
                elif sign == '-':
                    res.append(-num)
                elif sign == '*':
                    pre = res.pop()
                    res.append(num * pre)
                elif sign == '/':
                    pre = res.pop()
                    res.append(pre // num)
                sign = s[i]
            i += 1

        return sum(res)


x = Solution1()
s = "3+2*2" # 7
print(x.calculate(s))
s = "14-3/2"
print(x.calculate(s)) # 122
