class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        snums = sorted(nums)
        for i,v in enumerate(snums):
            if v not in d:
                d[v]=i
        return [ d[n] for n in nums ]