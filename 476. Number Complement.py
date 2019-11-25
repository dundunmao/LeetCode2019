# class Solution(object):
#     def findComplement(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         bn = bin(num)[2:]
#         oriList = list(bn)
#         rList = list()
#         for i in oriList:
#             if i == '0':
#                 rList.append('1')
#             else:
#                 rList.append('0')
#         r = ''.join(rList)
#         return int(r,2)
#
# class Solution1(object):
#     def findComplement(self, num):
#         i = 1
#         while i <= num:
#             i = i << 1
#         return (i - 1) ^ num
# x = Solution1()
# print(x.findComplement(5))
def gameWinner(colors):
    # Write your code here
    wendy = 0
    bob = 0
    count_w = 0
    count_b = 0
    i = 0
    while i < len(colors):
        if colors[i] == 'w':
            count_w = 0
            while i < len(colors) and colors[i] == 'w':
                count_w += 1
                i += 1
            if count_w > 2:
                wendy += count_w - 2
        elif colors[i] == 'b':
            count_b = 0
            while i < len(colors) and colors[i] == 'b':
                count_b += 1
                i += 1
            if count_b > 2:
                bob += count_b - 2
    return wendy >= bob
a = 'wwwbb'
print(gameWinner(a))
a = 'wwwbbb'
print(gameWinner(a))
a = 'wwwbbbbwww'
print(gameWinner(a))
