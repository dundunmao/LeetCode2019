class Solution:
    def calculate(self, s: str) -> int:
        if s == '' or len(s) == 0:
            return 0
        stack = []
        res = 0
        sign = 1
        i = 0
        num = 0
        while i < len(s):
        # for i in range(len(s)):
            if s[i].isdigit():
                num = int(s[i])
                while i + 1 < len(s) and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
                res += sign * num
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                res = 0 #从0开始累加
                sign = 1
            elif s[i] == ')':
                sign = stack.pop()
                num = stack.pop()
                res = res * sign + num
            i += 1
        return res


class Solution1:
    def calculate(self, s: str) -> int:
        if s == '' or len(s) == 0:
            return 0
        stack = []
        stack.append(Node())  # add dummy node
        i = 0
        while i < len(s):
            if s[i] == '(':
                node = Node()
                stack.append(node)
                i += 1
            elif s[i] == ')':
                cur = stack.pop()
                if cur.op == '+':
                    cur.res += cur.pre
                else:
                    cur.res -= cur.pre
                stack[-1].pre = cur.res
                i += 1
            elif s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                cur_num = int(s[start: i])
                stack[-1].pre = cur_num
            elif s[i] == '+' or s[i] == '-':
                pre_node = stack[-1]
                if pre_node.op == '+':
                    pre_node.res += pre_node.pre
                else:
                    pre_node.res -= pre_node.pre
                pre_node.pre = 0
                pre_node.op = s[i]
                i += 1
            else:
                i += 1
        res = stack[-1]
        if res.op == '+':
            return stack[-1].res + stack[-1].pre
        else:
            return stack[-1].res - stack[-1].pre


class Node:
    def __init__(self):
        self.res = 0
        self.op = '+'
        self.pre = 0

x = Solution1()
s = "-(12345+(4+5+2))" #-12356
print(x.calculate(s))
s = "(1+(4+5+2)-3)+(6+8)"
print(x.calculate(s)) # 23
s = "(100+(4+5+2)-3)+(6+8)"
print(x.calculate(s)) # 122
