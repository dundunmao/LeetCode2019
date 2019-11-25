class Solution:
    def toHex1(self, num: int) -> str:
        string_set = '0123456789abcdef'
        res = []
        while num > 0:
            res.append(string_set[num % 16])
            num = num // 16
        res.reverse()
        return ''.join([str(ele) for ele in res])



    def toHex(self, num):
        if num==0: return '0'
        mp = '0123456789abcdef'  # like a map
        ans = ''
        for i in range(8):
            n = num & 15    # num % 16   # this means num & 1111b
            c = mp[n]          # get the hex char
            ans = c + ans
            num = num >> 4   # num // 16
        return ans.lstrip('0')

s = Solution()
a = 26
print(s.toHex(a))
