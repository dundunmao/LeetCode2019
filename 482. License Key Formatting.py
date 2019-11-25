class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        res = []
        array = []
        for i in range(len(S) - 1, -1, -1):
            if S[i] != '-':
                array.append(S[i].upper())
                if len(array) == K:
                    res.insert(0, ''.join(array[::-1]))
                    array = []
        if len(array) != 0:
            res.insert(0, ''.join(array[::-1]))
        return '-'.join(res)

s = Solution()
# S ="5F3Z-2e-9-w"
# K = 4
# print(s.licenseKeyFormatting(S,K)) # "5F3Z-2E9W"
S ="2-5g-3-J"
K = 2
print(s.licenseKeyFormatting(S,K)) #"2-5G-3J"

