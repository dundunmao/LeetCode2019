class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ele_to_freq_hash = collections.Counter(nums)
        prev = None
        not_rob = 0
        rob = 0
        for num in sorted(ele_to_freq_hash):
            temp_not_rob = not_rob
            temp_rob = rob
            if num - 1 != prev: # 跟前面没连上
                not_rob = max(temp_not_rob, temp_rob)
                rob = num * ele_to_freq_hash[num] + max(temp_not_rob, temp_rob)
            else:
                not_rob = max(temp_not_rob, temp_rob)
                rob = num * ele_to_freq_hash[num] + temp_not_rob
            prev = num
        return max(not_rob, rob)
