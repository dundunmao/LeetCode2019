class Solution:
    # @return an integer
    def myAtoi(self, str):
        str = str.strip()  #去掉所有空格
        if len(str) == 0:
            return 0
        tmp = ""
        result = 0
        i = 0
        sign = 1
        if str[0] == "-":  #处理正负号
            sign = -1
            i = 1
        if str[0] == "+":  #处理正负号
            i = 1
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        for i in range(i, len(str)):  #把digit的取出来，遇到非digit的break
            if str[i].isdigit():
                tmp += str[i]
            else:
                break
        if len(tmp) > 0:         #计算长度
            result = sign * int(tmp)
        if result > MAX_INT > 0:   #处理溢出情况
            return MAX_INT
        elif result < MIN_INT < 0:
            return MIN_INT
        else:
            return result

# class Solution(object):
#     def myAtoi(self, str):
#         """
#         :type str: str
#         :rtype: int
#         """
#         if str == '' or str is None:
#             return 0
#         str.strip()
#         i = 0
#         while str[0] == '-' or str[0] == '+' or str[i] == '0' or not str[i].isdigit():
#             if str[0] == '-' or str[0] == '+' or str[i] == '0':
#                 i += 1
#             if i > len(str)-1:
#                 break
#             if i < len(str) and not str[i].isdigit():
#                 return 0
#
#         le = 0
#         j = i
#         nums = 0
#         while j < len(str):
#             if str[j].isdigit():
#                 le += 1
#                 j += 1
#             else:
#                 break
#
#         for k in range(i, i + le):
#             nums += int(str[k]) * 10 ** (le - 1)
#             # print nums
#             le -= 1
#
#         if str[0] == '-':
#             return -nums
#         else:
#             return nums

if __name__ == "__main__":

    # s = "12"
    s = "-3.14159"
    x = Solution()
    print(x.myAtoi(s))
