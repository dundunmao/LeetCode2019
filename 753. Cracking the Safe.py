class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        total_size = k ** n
        ans = ['0'] * n
        visited = set()
        visited.add(''.join(ans))
        if self.dfs(ans, total_size, n, k, visited):
            return ''.join(ans)
        return ''

    def dfs(self, ans, total_size, n, k, visited):
        if len(visited) == total_size:
            return True
        node = ans[len(ans) - n + 1:len(ans)] #上一个密码的n-1位
        for c in range(k):
            node.append(str(c))
            node_string = ''.join(node)
            if node_string not in visited:
                ans.append(str(c))
                visited.add(node_string)
                if self.dfs(ans, total_size, n, k, visited):
                    return True
                visited.remove(node_string)
                ans.pop()
            node.pop()
        return False

s = Solution()
# n = 1
# k = 2
# print(s.crackSafe(n, k))
n = 2
k = 2
print(s.crackSafe(n, k))

