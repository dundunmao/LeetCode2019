# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root):
        visited = {}
        self.dfs(root, 0, 0, visited)
        ans = []
        sorted_x = sorted(visited.keys())

        for x in sorted_x:
            report = []
            sorted_y = sorted(visited[x].keys())
            for y in sorted_y:
                report.extend(visited[x][y])
            ans.append(report)

        return ans

    def dfs(self, node, x, y, visited):
        if node:
            if x in visited:
                if y not in visited[x]:
                    visited[x][y] = [node.val]
                else:
                    visited[x][y].append(node.val)
            else:
                visited[x] = {}
                visited[x][y] = [node.val]
            self.dfs(node.left, x - 1, y + 1, visited)
            self.dfs(node.right, x + 1, y + 1, visited)
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.left.left = TreeNode(4)
p.left.right = TreeNode(5)
p.right.left = TreeNode(6)
p.right.right = TreeNode(7)
s = Solution()
print(s.verticalTraversal(p))

