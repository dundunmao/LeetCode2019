# 给定 n 对括号，请写一个函数以将其生成新的括号组合，并返回所有组合结果。
# Example
# 给定 n = 3, 可生成的组合如下:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"



class Solution1(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        str = ''
        left = 0
        right = 0
        self.helper(res, str, left, right, n)
        return res

    def helper(self, res, str, left, right, n):  # 按一定规则往str里加左右括号，一旦right到n了，就放res里
        if right == n:
            res.append(str)
            return
        # 下面分两支
        if left < n:  # 如果left没都用了时，就加left
            self.helper(res, str+'(', left + 1, right, n)
        if right < left:  # 同时如果right比left少时，就加right
            self.helper(res, str+')', left, right + 1, n)

class TreeNode():  #node为啥括号，到目前位置left几个了，right几个了
    def __init__(self,par,left_num,right_num):
        self.type = par
        self.left = left_num
        self.right = right_num
class Solution(object):
    def generateParenthesis(self, n):
        res = []
        if n <= 0:
            return res
        array = ['' for i in range(2*n)] #往里面加的括号的样子
        stack = []
        root = TreeNode('(', 1, 0) #initial放一个"("
        stack.append(root)

        while len(stack) != 0:
            node = stack.pop()

            #  op at node
            array[node.left + node.right - 1] = node.type #把pop出来括号放在对应的位置
            if node.left == n and node.right == n: #如果左右括号都满了，就是找到了，放结果了
                res.append(''.join(array))

            # 生孩子
            if node.left < n: #如果left没满
                stack.append(TreeNode('(', node.left + 1, node.right))
            if node.right < node.left:  #➡️ right少于left时，加right
                stack.append(TreeNode(')', node.left, node.right+1))
        return res



class Solution3(object):
    def generateParenthesis(self, n):
        res = []
        if n <= 0:
            return res
        array = ['' for i in range(2*n)] #往里面加的括号的样子
        stack = []
        root = ('(', 1, 0) #initial放一个"("
        stack.append(root)

        while len(stack) != 0:
            node = stack.pop()

            #  op at node
            array[node[1] + node[2] - 1] = node[0] #把pop出来括号放在对应的位置
            if node[1] == n and node[2] == n: #如果左右括号都满了，就是找到了，放结果了
                res.append(''.join(array))

            # 生孩子
            if node[1] < n: #如果left没满
                stack.append(('(', node[1] + 1, node[2]))
            if node[2] < node[1]:  #➡️ right少于left时，加right
                stack.append((')', node[1], node[2]+1))
        return res
#############

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        self.dfs(n, 1, 0, '(', res, path)
        return res
    # 算上'我'，左括号有多少，右括号有多少
    def dfs(self, n, left_count, right_count, paren, res, path):
        #进来加我
        path.append(paren)
        # 拿到valid答案
        if right_count == n and right_count == right_count:
            res.append(''.join(path))
        # 符合往左走的条件，往左走
        if left_count < n:
            self.dfs(n, left_count + 1, right_count, '(', res, path)
        # 符合往右走的条件，往右走
        if right_count < left_count:
            self.dfs(n, left_count, right_count + 1, ')', res, path)
        # 离开删我
        path.pop()


class Solution:
    def generateParenthesis(self, n: int):
        res = []
        path = []
        self.dfs(n, 0, 0, res, path)
        return res

    def dfs(self, n, l, r, res, path):
        if l == n and r == n:
            res.append(''.join(path))
            return
        if l < n:
            path.append('(')
            self.dfs(n, l + 1, r, res, path)
            path.pop()
        if l > r:
            path.append(')')
            self.dfs(n, l, r + 1, res, path)
            path.pop()
if __name__ == "__main__":
    n = 3
    s = Solution3()

    print(s.generateParenthesis(n))
