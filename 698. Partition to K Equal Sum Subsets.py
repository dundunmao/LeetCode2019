class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 先看每个bucket需要多少sum
        sum_up = sum(nums)
        if sum_up % k != 0:
            return False
        sub_sum = sum_up // k
        # sort之后从后往前看，排除最大的数查sub-sum了，并把==sub_sum的数自己放一个bucket里，这样k--
        nums.sort()
        pos = len(nums) - 1
        if nums[pos] > sub_sum:
            return False
        while pos >= 0 and nums[pos] == sub_sum:
            pos -= 1
            k -= 1
        if k == 0:
            return True
        # 从后往前遍历num，把num试图往每一个bucket里装，再往下放下一个num，如果num都能放进去，就是True
        k_bucket = [0 for i in range(k)]
        return self.dfs(k_bucket, nums, pos, sub_sum)

    def dfs(self, k_bucket, nums, pos, sub_sum):
        if pos < 0:
            return True
        selected = nums[pos]
        for i in range(len(k_bucket)):
            if k_bucket[i] + selected <= sub_sum:
                k_bucket[i] += selected
                if self.dfs(k_bucket, nums, pos - 1, sub_sum):
                    return True
                k_bucket[i] -= selected
        return False

