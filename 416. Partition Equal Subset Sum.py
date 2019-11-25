class Solution:
    def canPartition(self, nums) -> bool:
        sum_up = sum(nums)
        if sum_up % 2 != 0:
            return False

        dp = [[False] * (sum_up // 2 + 1) for i in range(len(nums) + 1)]
        for j in range(0, sum_up // 2 + 1):
            for i in range(0, len(nums) + 1):
                if j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = False
                else:
                    if j - nums[i - 1] >= 0 and dp[i - 1][j - nums[i - 1]]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i - 1][j]

        for i in range(1, len(nums) + 1):
            if dp[i][sum_up // 2]:
                return True
        return False

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_up = sum(nums)
        if sum_up % 2 != 0:
            return False
        target = sum_up // 2
        visited = {}
        return self.dfs(nums, 0, target, visited)

    def dfs(self, nums, index, target, visited):
        if (index, target) in visited:
            return visited[(index, target)]
        # base case
        if target == 0:
            visited[(index, target)] = True
            return True
        if index == len(nums) or target < 0:
            visited[(index, target)] = False
            return False
        # general case
        if self.dfs(nums, index + 1, target - nums[index], visited):
            visited[(index, target)] = True
            return True

        if self.dfs(nums, index + 1, target, visited):
            visited[(index, target)] = True
            return True

        visited[(index, target)] = False
        return False

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_up = sum(nums)
        if sum_up % 2 != 0:
            return False
        target = sum_up // 2
        n = len(nums)
        dp = [[False] * (target + 1) for i in range(n + 1)]
        for i in range(0, n + 1):
            for j in range(0, target + 1):
                if j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = False
                else:
                    if j - nums[i - 1] >= 0:
                        dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
            if dp[i][target]:
                return True
        return False

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_up = sum(nums)
        if sum_up % 2 != 0:
            return False
        target = sum_up // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, -1, -1):
                if j >= num:
                    dp[j] = dp[j] or dp[j - num] # 选他或不选他
        return dp[target]


s = Solution()
a = [1,2,5]
print(s.canPartition(a))
a = [23,13,11,7,6,5,5]
print(s.canPartition(a))

a = [1, 5, 11, 5]
print(s.canPartition(a))

