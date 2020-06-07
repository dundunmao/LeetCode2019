class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        memo = {}
        res = self.dfs(0, -100, 0, target, houses, cost, m, n, memo)
        if res == float('inf'):
            return -1
        else:
            return res

    def dfs(self, pos, pre_color, neighborhood, target, houses, cost, m, n, memo):
        if (pos, pre_color, neighborhood) in memo:  # 有memo
            return memo[(pos, pre_color, neighborhood)]
        if neighborhood > target:  # group个数超过target
            memo[(pos, pre_color, neighborhood)] = float('inf')
            return float('inf')
        if pos == len(houses):  # 所有房子都遍历完，叶子节点的下一个，None节点
            if neighborhood == target:
                memo[(pos, pre_color, neighborhood)] = 0
                return 0
            else:
                memo[(pos, pre_color, neighborhood)] = float('inf')
                return float('inf')
        # 开始分叉处理
        res = float('inf')
        # 先是已经涂色了的，就跳过他去下一个叶子
        if houses[pos] != 0:
            if houses[pos] != pre_color:
                new_neigh = neighborhood + 1
            else:
                new_neigh = neighborhood
            res = self.dfs(pos + 1, houses[pos], new_neigh, target, houses, cost, m, n, memo)
        # 没涂色的，就遍历一遍n个颜色，找返回值最小的return
        else:
            for i in range(n):
                costs = cost[pos][i]
                if pre_color == i + 1:
                    now_neigh = neighborhood
                else:
                    now_neigh = neighborhood + 1
                res = min(res, costs + self.dfs(pos + 1, i + 1, now_neigh, target, houses, cost, m, n, memo))
        memo[(pos, pre_color, neighborhood)] = res
        return res