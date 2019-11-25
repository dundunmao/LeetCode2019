class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        len_d = len(coins)
        coins.sort()
        f = [[ float('inf') for i in range(amount+1)] for k in range(len_d+1)]
        for k in range(0,len_d + 1):
            f[k][0] = 0
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if j-coins[i-1] >= 0:
                    f[i][j] = min(f[i-1][j],f[i][j-coins[i-1]]+1)
                else:
                    f[i][j] = f[i - 1][j]
        return f[len_d][amount] if f[len_d][amount] != float('inf') else -1
#     滚动数组优化
class Solution1(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        f = [[ float('inf') for i in range(amount+1)] for k in range(2)]
        for k in range(2):
            f[k][0] = 0
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if j-coins[i-1] >= 0:
                    f[i%2][j] = min(f[(i-1)%2][j],f[i%2][j-coins[(i-1)]]+1)
                else:
                    f[i%2][j] = f[(i-1)%2][j]
        return f[(i)%2][amount] if f[(i)%2][amount] != float('inf') else -1
 #################
 # DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        f = [float('inf') for i in range(amount + 1)]
        f[0] = 0 # 0 个coin 组成0的amount
        for i in range(0, len(coins)):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0: #如果当前的coin可以用
                    f[j] = min(f[j], f[j - coins[(i)]] + 1) # 用掉当前的coin和之前算好的，取最小
        return f[amount] if f[amount] != float('inf') else -1
# BFS
import collections
class Solution3:
    def coinChange(self, coins, amount: int) -> int:
        queue = collections.deque()
        left = amount
        level = 0
        queue.append((left, level))
        visited = set()
        visited.add(left)
        while len(queue) > 0:
            left, level = queue.popleft()
            level += 1
            for coin in coins:
                temp = left - coin
                if temp < 0:
                    continue
                elif temp == 0:
                    return level
                elif temp not in visited:
                    queue.append((temp, level))
                    visited.add(temp)
        return -1
# DFS
class Solution4:
    def coinChange(self, coins, amount: int) -> int:
        left_to_level = {}
        left_to_level[0] = 0

        return self.dfs(coins, amount, left_to_level)

    def dfs(self, coins, left, left_to_level):
        if left < 0:
            return -1
        if left in left_to_level:
            level = left_to_level[left]
            return level
        cur_level = float('inf')
        for coin in coins:
            temp_left = left - coin
            child = self.dfs(coins, temp_left, left_to_level)
            if child >= 0:
                cur_level = min(cur_level, child + 1)
        left_to_level[left] = cur_level
        return -1 if cur_level == float('inf') else cur_level

if __name__ == "__main__":
    s = Solution4()
    a = [1,10]
    b = 2
    print(s.coinChange(a, b)) #2

    a = [1, 2, 5]
    b = 11
    print(s.coinChange(a, b)) #3
    a = [1, 2]
    b = 3
    print(s.coinChange(a, b)) #2
    a = [28,104,259,357,346,107,413,497,241,423]

    b = 1795
    print(s.coinChange(a, b)) #5
