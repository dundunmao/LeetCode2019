class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_group = self.group(name)
        typed_group = self.group(typed)
        if len(name_group) != len(typed_group):
            return False
        for n, y in zip(name_group, typed_group):
            if n[0] != y[0]:
                return False
            if n[1] > y[1]:
                return False
        return True

    def group(self, string):
        res = []
        start = 0
        i = 0
        while i < len(string):
            while i < len(string) and string[i] == string[start]:
                i += 1
            res.append((string[start], i - start))
            start = i
            i = start
        return res
s = Solution()

name = "pyplrz"
typed = "ppyypllr"
print(s.isLongPressedName(name,typed))

name = "alex"
typed = "aaleex"
print(s.isLongPressedName(name,typed))
name = "saeed"
typed = "ssaaedd"
print(s.isLongPressedName(name,typed))
name = "leelee"
typed = "lleeelee"
print(s.isLongPressedName(name,typed))
