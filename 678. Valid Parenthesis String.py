class Solution:
    def checkValidString(self, s: str) -> bool:
        lower = 0
        upper = 0
        for c in s:
            if c == '(':
                lower += 1
                upper += 1
            elif c == ')':
                lower -= 1
                upper -= 1
                if lower < 0:
                    lower = 0
            elif c == '*':
                lower -= 1
                upper += 1
                if lower < 0:
                    lower = 0
            if upper < 0:
                return False
        return lower == 0
s = Solution()
# a = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
# # a = "(((*)(*)((*"
# print(s.checkValidString(a)) #F
# a = "()"
# print(s.checkValidString(a)) #T
# a = "(*))"
# print(s.checkValidString(a)) #T
# a = "(*)"
# print(s.checkValidString(a)) #T
a = "(*))()"
print(s.checkValidString(a)) #T
a = "(((******))"
print(s.checkValidString(a)) #T
a = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
print(s.checkValidString(a)) #T
