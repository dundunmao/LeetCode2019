# dp
class Solution(object):
    def longestValidParentheses(self, s):
        res = 0
        n = len(s)
        f = [0 for i in range(n)]
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    if i > 1:
                        f[i] = f[i-2] + 2
                    else:
                        f[i] = 2
                elif i - f[i - 1] -1 >= 0 and s[i - f[i - 1] - 1] == '(':
                    if i > 1:
                        f[i] = f[i - 1] + f[i - f[i - 1] - 2] + 2
                    else:
                        f = f[i - 1] + 2
            res = max(res, f[i])
        return res
# DP,只是调整了一下让f = n+1的长度
class Solution2(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n = len(s)
        f = [0 for i in range(n + 1)]
        f[0] = 0
        for i in range(1, n + 1):
            if i == 1:
                f[i] = 0
                continue
            if s[i - 1] == ')':
                if s[i - 2] == '(':
                    f[i] = f[i - 2] + 2
                elif i - f[i - 1] - 1 >= 0 and s[i - f[i - 1] - 2] == '(':
                    f[i] = f[i - 1] + f[i - f[i - 1] - 2] + 2
            res = max(res, f[i])
        return res
# stack
class Solution1(object):
    def longestValidParentheses(self, s):
        res = 0
        stack = []
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack==[]:
                    stack.append(i)
                else:
                    res = max(res,i-stack[-1])
        return res



class Solution3:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        res = 0
        # left -> right
        left = 0
        right = 0
        start = 0
        for j in range(0, n):
            if s[j] == '(':
                left += 1
            else:
                right += 1
                if left == right:
                    res = max(res, j - start + 1)
                elif right > left:
                    start = j + 1
                    left = 0
                    right = 0
        # right -> left
        left = 0
        right = 0
        end = n - 1
        for i in range(n - 1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
                if left == right:
                    res = max(res, end - i + 1)
                elif left > right:
                    end = i - 1
                    left = 0
                    right = 0
            i -= 1
        return res

class Solution4:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        res = 0
        left = 0
        right = 0
        i = 0
        j = 0
        while i < len(s) and j < len(s):
            if s[j] == '(':
                left += 1
            else:
                right += 1
                if left == right:
                    res = max(res, j - i + 1)
                elif right > left:
                    i = j + 1
                    left = 0
                    right = 0

            j += 1
        new_i = len(s) - 1
        new_j = len(s) - 1
        left = 0
        right = 0

        while new_i >= 0 and new_j >= 0:
            if s[new_j] == ')':
                right += 1
            else:
                left += 1
                if left == right:
                    res = max(res, new_i - new_j + 1)
                elif left > right:
                    new_i = new_j - 1
                    left = 0
                    right = 0
            new_j -= 1
        return res


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s)
        res = 0
        start_track = [i for i in range(n)]
        if s[0] == '(':
            start_track[0] = 0
        else:
            start_track[0] = 1
        for i in range(1, n):
            if s[i] == '(':
                if s[i - 1] == ')':
                    start_track[i] = start_track[i - 1]
                else:
                    start_track[i] = i
            else:
                if s[i - 1] == ')':
                    if start_track[i - 1] - 1 >= 0 and s[start_track[i - 1] - 1] == '(':
                        start_track[i] = start_track[start_track[i - 1] - 1]
                    else:
                        start_track[i] = i + 1
                else:
                    start_track[i] = start_track[i - 1]
                res = max(res, i - start_track[i] + 1)
        return res
class Solution11:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s)
        res = 0
        stack = []
        temp = 0
        for i in range(0, n):
            if s[i] == ')':
                if len(stack) == 0:
                    res = max(res, temp)
                    temp = 0
                    continue
                elif stack[-1] == '(':
                    stack.pop()
                    temp += 2
                    res = max(res, temp)
            else:
                stack.append('(')
        return res

class Solution12:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s)
        res = 0
        stack = []
        count = 0
        start = -1
        for i in range(0, n):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                count -= 1
            if count == 0:
                res = max(res, i - start)
            if count == -1:
                start = i
                count = 0
        return res


if __name__ == '__main__':
    s = Solution12()
    # board = "()" # 2
    # print(s.longestValidParentheses(board))
    # board = "((()))()((" #8
    # print(s.longestValidParentheses(board))
    board = "(((()))" #6
    print(s.longestValidParentheses(board))
    board = ")()())" #4
    print(s.longestValidParentheses(board))
    board = "(()" #2
    print(s.longestValidParentheses(board))
    board = "(()()"#4
    print(s.longestValidParentheses(board))
    board = ")(((((()())()()))()(()))(" #22
    print(s.longestValidParentheses(board))




