# dfs超时
class Solution:
    def __init__(self):
        self.result = 0
    def findTargetSumWays(self, nums, S: int) -> int:
        pos = 0
        sum_up = 0

        self.helper(nums,S,pos,sum_up)
        return self.result
    def helper(self,nums,S,pos,sum_up): #以pos为起点能达到sum_up的各数
        if pos == len(nums):
            if sum_up==S:
                self.result += 1
            return

        self.helper(nums,S,pos+1,sum_up-nums[pos])
        self.helper(nums,S,pos+1,sum_up+nums[pos])

# dfs + memo
class Solution:
    def findTargetSumWays(self, nums, S):
        memo = [[float('-inf') for i in range(2001)] for j in range(len(nums))]
        # pos为0时，pos之前的sum为0
        return self.dfs(nums, 0, 0, S, memo)

    # return 在pos节点，sum_up不包括pos时的方式有多少
    def dfs(self, nums, pos, sum_up, S, memo):
        # 越界在None的时候
        if pos == len(nums):
            if sum_up == S:
                return 1
            else:
                return 0

        if memo[pos][sum_up + 1000] != float('-inf'):
            return memo[pos][sum_up + 1000]

        plus = self.dfs(nums, pos + 1, sum_up + nums[pos], S, memo)
        minus = self.dfs(nums, pos + 1, sum_up - nums[pos], S, memo)
        memo[pos][sum_up + 1000] = plus + minus
        return memo[pos][sum_up + 1000]
# dp
class Solution2(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # 因为sum不超过1000，正负就为2000.len(nums)行，sum列
        dp = [[0 for i in range(2001)] for j in range(len(nums))]
        # 找中间的位置，黄色
        # dp[i][j]表示 （0~i）这段数能组成sum=j的方式有多少种
        # 最后要找 i= len(nums)-1, j = S+1000（因为起始位置是-1000，然后还有0）
        dp[0][nums[0] + 1000] = 1  #sum = nums[0]的方式有1种
        dp[0][-nums[0] + 1000] += 1 #sum = -nums[0]的方式有+1种这里因为有nums[0]=0的情况，这样就是1+1=2了
        for i in range(1, len(nums)):
            for sum in range(-1000, 1001):
                if dp[i - 1][sum + 1000] > 0:
                    dp[i][sum + nums[i] + 1000] += dp[i - 1][sum + 1000] #紫色+部分，就是上一个位置+了nums[i]
                    dp[i][sum - nums[i] + 1000] += dp[i - 1][sum + 1000] #绿色-部分,就是上一个位置-了nums[i]

        return 0 if S > 1000 else dp[len(nums) - 1][S + 1000]
class Solution3(object):
    def findTargetSumWays(self, nums, S):
        dp = [0 for i in range(2001)]
        dp[nums[0] + 1000] = 1
        dp[-nums[0] + 1000] += 1
        for i in range(1,len(nums)):
            next = [0 for _ in range(2001)]
            for sum in range(-1000, 1001):
                if dp[sum + 1000] > 0:
                    next[sum + nums[i] + 1000] += dp[sum + 1000]
                    next[sum - nums[i] + 1000] += dp[sum + 1000]
            dp = next
        return 0 if S > 1000 else dp[S + 1000]

if __name__ == '__main__':
    s = Solution5()
    a = [1,1,1,1,1]
    X = 3
    print(s.findTargetSumWays(a,X))
