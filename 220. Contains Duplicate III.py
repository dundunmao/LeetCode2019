class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) == 0 or k <= 0 or t < 0:
            return False
        mini = min(nums)
        bucket_hash = {}
        for i in range(len(nums)):
            index = (nums[i] - mini) // (t + 1)
            if index in bucket_hash and i - bucket_hash[index] <= k:
                return True
            else:
                if index - 1 in bucket_hash and abs(nums[bucket_hash[index - 1]] - nums[i]) <= t and i - bucket_hash[
                    index - 1] <= k:
                    return True
                if index + 1 in bucket_hash and abs(nums[bucket_hash[index + 1]] - nums[i]) <= t and i - bucket_hash[
                    index + 1] <= k:
                    return True
                bucket_hash[index] = i
        return False


