class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if len(nums) == 0:
            cur = self.group(lower, upper)
            return [cur]
        res = []
        # base case
        if nums[0] != lower:
            cur = self.group(lower, nums[0] - 1)
            res.append(cur)
        # general case
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1 and nums[i] != nums[i - 1]:
                cur = self.group(nums[i - 1] + 1, nums[i] - 1)
                res.append(cur)
        # 收尾
        if nums[-1] != upper:
            cur = self.group(nums[-1] + 1, upper)
            res.append(cur)
        return res

    def group(self, start, end):
        if start == end:
            return str(end)
        else:
            return str(start) + '->' + str(end)
