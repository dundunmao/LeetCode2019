import collections


class Solution2(object):
    def removeInvalidParentheses(self, s):
        res = []
        last_i, last_j = 0, 0
        par = ['(', ')']
        self.helper(s, res, last_i, last_j, par)
        return res

    def helper(self, s, res, last_i, last_j, par):
        count = 0
        for i in range(last_i, len(s)):  # i开始遍历，直到找到一个多余的右括号，就把这个右括号去掉，然后继续往下遍历
            if s[i] == par[0]:
                count += 1
            if s[i] == par[1]:
                count -= 1
            if count >= 0:
                continue
            for j in range(last_j, i + 1):
                # 前面是open，j是close，或者j是close并且把头，因为我这轮是要取右括号，所以，下面就把这个右括号j去掉，看剩下的啥情况
                if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):  #看遍历的这个j是不是右，并且或者j是把头的，或者j-1不是右，就是它是不是起点时，他前面那个是个open
                    self.helper(s[:j] + s[j + 1:], res, i, j, par)  #在i~j这一段，除去这个j的剩下合一起，看有啥能valid的组合
            return
        if s:
            reverse = s[::-1]
            if par[0] == '(':
                self.helper(reverse, res, 0, 0, [')', '('])
            else:
                res.append(reverse)
        else:
            res.append(s)
class Solution_one_case(object):
    def removeInvalidParentheses(self, s):
        s = list(s)
        l = '('
        r = ')'
        c_left = 0
        c_right = 0
        res = []
        i = 0
        while i < len(s):
            if s[i] == l:
                c_left += 1
            elif s[i] == r:
                c_right += 1
            if c_right>c_left:
                del s[i]
                c_right -= 1
            else:
                i += 1
        j = len(s)-1
        c_left = 0
        c_right = 0
        while j >=0:
            if s[j] == l:
                c_left += 1
            elif s[j] == r:
                c_right += 1
            if c_right < c_left:
                del s[j]
                c_left -= 1
                j -= 1
            else:
                j -= 1
        return ''.join(s)

class Solution_one_case1(object):
    def removeInvalidParentheses(self, s):
        left = 0
        deleted_list = set()# 把需要删除的都加到这里
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                if left == 0:
                    deleted_list.add(i)
                else:
                    left -= 1
        for i in range(len(s) - 1, -1, -1):
            if left == 0:
                break
            elif s[i] == '(':
                deleted_list.add(i)
                left -= 1
        ans = []
        for i in range(len(s)):
            if i not in deleted_list:
                ans.append(s[i])
        return ''.join(ans)


###############
# DFS
class Solution5(object):
    def removeInvalidParentheses(self, s):
        l = 0
        r = 0
        for cha in s:
            if cha == '(':
                l += 1
            if cha == ')':
                if l == 0:
                    r += 1
                else:
                    l -= 1
        ans = []
        s_array = list(s)
        self.dfs(s_array, 0, l, r, ans)
        return ans
    def dfs(self, s_array, start, l, r, ans):
        if l == 0 and r == 0:
            s = ''.join(s_array)
            if self.isValid(s):
                ans.append(s)
            return
        for i in range(start, len(s_array)):
            if i != start and s_array[i] == s_array[i - 1]:
                continue
            if r > 0:
                if s_array[i] == ')':
                    curr = s_array[:i] + s_array[i + 1:]
                    self.dfs(curr, i, l, r - 1, ans)
            else:

                if s_array[i] == '(':
                    curr = s_array[:i] + s_array[i + 1:]
                    self.dfs(curr, i, l - 1, r, ans)

    def isValid(self, s):
        count = 0
        for i in range(0, len(s)):
            c = s[i]
            if c == '(':
                count += 1
            if c == ')':
                if count == 0:
                    return False
                else:
                    count -= 1
        return count == 0



# BFS

class Solution:
    def removeInvalidParentheses(self, s):
        res = []
        if s is None:
            return res
        visited = set()
        q = collections.deque()
        q.append(s)
        visited.add(s)
        while len(q) != 0:
            cur = q.popleft()
            if self.isValid(cur):
                if len(res) > 0 and len(cur) < len(res[-1]):
                    return res
                res.append(cur)
                continue
            for i in range(len(cur)):
            # we only try to remove left or right paren
                if cur[i] == '(' or cur[i] == ')':
                    t = cur[:i] + cur[i+1:]
                    if t not in visited:
                        q.append(t)
                        visited.add(t)
        return res

    def isValid(self, s):
        count = 0
        for i in range(0, len(s)):
            c = s[i]
            if c == '(':
                count += 1
            if c == ')':
                if count == 0:
                    return False
                else:
                    count -= 1
        return count == 0
if __name__ == "__main__":
    s = Solution_one_case1()
    # s = Solution()
    # str = '())))(('
    # print(s.removeInvalidParentheses(str))
    # str = '()())()'
    # print(s.removeInvalidParentheses(str))
    str = "(a)())()"
    print(s.removeInvalidParentheses(str))
    str = ")("
    print(s.removeInvalidParentheses(str))


