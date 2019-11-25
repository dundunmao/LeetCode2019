class Solution:
    def convertToTitle(self, n: int) -> str:
        string_builder = []
        while n > 0:
            # n -= 1
            cur = chr(n % 26 + 65 -1)
            string_builder.append(cur)
            n = n // 26

        string_builder.reverse()
        return ''.join(string_builder)

s = Solution()
# print(s.convertToTitle(701))#ZY
print(s.convertToTitle(26))#ZY
print(s.convertToTitle(1))#A
print(s.convertToTitle(28))#AB
print(s.convertToTitle(1048)) # ANH
