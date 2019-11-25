class Solution:
    def removeStones(self, stones) -> int:
        n = len(stones)
        dsu = DSU(n)
        for i in range(n):
            for j in range(i + 1, n):
                # 任选两个石头，如果在同一行或同一列，就连起来
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    dsu.union(i, j)
        return n - dsu.count


class DSU:
    def __init__(self, n):
        self.size = [0 for i in range(n)]
        self.root = [0 for i in range(n)]
        self.count = n
        #开始自己就是自己的根
        for i in range(n):
            self.root[i] = i

    def find(self, x):
        if self.root[x] != x: # 如果自己不是自己的根
            self.root[x] = self.find(self.root[x]) # x的根就是
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x) #找到x石头的根
        root_y = self.find(y) #找到y石头的根
        if root_x == root_y: #如果根一样，就不管了
            return
        if self.size[root_x] <= self.size[root_y]: #如果x的根对应的图size小，就把x的图接到y的图上，y的图的size+1
            self.root[root_x] = root_y
            self.size[root_y] += 1
        else:
            self.root[root_y] = root_x
            self.size[root_x] += 1
        self.count -= 1 # 图的各数少了一个

## dfs
import collections
class Solution1(object):
    def removeStones(self, stones):
        points = {(i, j) for i, j in stones}
        island = 0
        # 把每个 row 里的所有 col 都放一起
        rows = collections.defaultdict(list)
        # 把每个 col 里的所有 row 都放一起
        cols = collections.defaultdict(list)
        # 把每个row里的所有 col 都放一起
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)

        for i, j in stones:
            if (i, j) in points:
                # 把这一片连通图找到
                self.dfs(i, j, points, rows, cols)
                island += 1
        return len(stones) - island
    # 以（i，j）为起点去删他所在行和列的所有点，全部删完，这一块大陆就走完了
    def dfs(self, i, j, points, rows, cols):
        points.discard((i, j))
        for y in rows[i]:
            if (i, y) in points:
                self.dfs(i, y, points, rows, cols)
        for x in cols[j]:
            if (x, j) in points:
                self.dfs(x, j, points, rows, cols)
s = Solution()
a = [[0,0],[0,2],[1,1],[2,0],[2,2],[1,3]]
print(s.removeStones(a))

a = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
