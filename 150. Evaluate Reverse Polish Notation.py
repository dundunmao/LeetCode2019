class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for ele in tokens:
            if ele == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif ele == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif ele == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif ele == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1 / num2))
            else:
                stack.append(int(ele))
        return stack.pop()
x = Solution()
a = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(x.evalRPN(a))
