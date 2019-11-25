class Solution:
    def singleNumber(self, nums):
        bit = [0] * 32
        for num in nums:
            for i in range(32):
                bit[i] += num >> i & 1
        res = 0
        for i, val in enumerate(bit):
            # if the single numble is negative,
            # this case should be considered separately
            if i == 31 and val%3:
                res = -((1<<31)-res)
            else:
                res |= (val%3)*(1<<i)
        return res

