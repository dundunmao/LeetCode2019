class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = [0] * len(nums)
        start = 0
        end = len(nums) - 1
        if a >= 0:
            i = end
            while start <= end:
                start_nums = self.calculate(nums[start], a, b, c)
                end_nums = self.calculate(nums[end], a, b, c)
                if start_nums >= end_nums:
                    res[i] = start_nums
                    start += 1
                else:
                    res[i] = end_nums
                    end -= 1
                i -= 1
        else:
            i = 0
            while start <= end:
                start_nums = self.calculate(nums[start], a, b, c)
                end_nums = self.calculate(nums[end], a, b, c)
                if start_nums <= end_nums:
                    res[i] = start_nums
                    start += 1
                else:
                    res[i] = end_nums
                    end -= 1
                i += 1
        return res

    def calculate(self, num, a, b, c):
        return a * num * num + b * num + c     
