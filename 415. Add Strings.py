class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        len_num1 = len(num1)
        len_num2 = len(num2)
        size = len_num1
        # 补齐长度
        if len_num1 < len_num2:
            size = len_num2
            num1 = '0' * (len_num2 - len_num1) + num1
        elif len_num2 < len_num1:
            size = len_num1
            num2 = '0' * (len_num1 - len_num2) + num2
        res = [0] * size
        # 开始算数
        for i in range(size - 1, -1, -1):
            sum_up = int(num1[i]) + int(num2[i]) + carry
            carry = sum_up // 10
            res[i] = str(sum_up % 10)

        if carry > 0:
            res.insert(0, str(carry))
        return ''.join(res)


s = Solution()
a = '99'
b = '99'
print(s.addStrings(a,b))
