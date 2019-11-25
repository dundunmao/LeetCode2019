class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if not S or len(S) == 0:
            return 0
        left = 0
        right = 0
        for cha in S:
            if cha == '(':
                right += 1
            else:
                if right > 0:
                    right -= 1
                else:
                    left += 1
        return left + right


# stack
    def minAddToMakeValid1(self, S: str):
        stack = []
        for cha in S:
            if cha == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(cha)
        return len(stack)

    def minAddToMakeValid2(self, S: str):
        while "()" in S:
            S = S.replace("()", "")
        return len(S)

