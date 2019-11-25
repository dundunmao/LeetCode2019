class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_parentheses = set()
        left = 0
        right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                if left == right:
                    remove_parentheses.add(i)
                    left == 0
                    right == 0
                else:
                    right += 1
        # print(remove_parentheses)
        left = 0
        right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                right += 1
            elif s[i] == '(':
                if left == right:
                    remove_parentheses.add(i)
                    left == 0
                    right == 0
                else:
                    left += 1
        # print(remove_parentheses)
        ans = []
        for i in range(len(s)):
            if i not in remove_parentheses:
                ans.append(s[i])
        return ''.join(ans)
