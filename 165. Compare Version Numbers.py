class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(max(len(v1), len(v2))):
            num1 = v1[i] if i < len(v1) else '0'
            num2 = v2[i] if i < len(v2) else '0'
            if int(num1) < int(num2):
                return -1
            elif int(num1) > int(num2):
                return 1
        return 0
s = Solution()
v1 = "1.01"
v2 = "1.001"
print((s.compareVersion(v1, v2)))
v1 = "1.0"
v2 = "1.0.0"
print((s.compareVersion(v1, v2)))
