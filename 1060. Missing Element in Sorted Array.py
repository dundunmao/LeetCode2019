
class Solution1:
    def missingElement(self, nums, k):
        # base case
        nums.append(float('inf'))
        count = 0
        record = 0
        cur = nums[0]
        # general case
        while count < k:
            if nums[record] != cur:
                count += 1
                cur += 1
            else:
                cur += 1
                record += 1
        return cur - 1
class Solution2:
    def missingElement(self, nums, k):
        new_array = []
        new_array.append(nums[0])
        for i in range(1, len(nums)):
            new_array.append(new_array[i-1] + 1)
        diff = []
        for i in range(len(nums)):
            diff.append(nums[i] - new_array[i])
        if k <= diff[-1]:
            start = self.find_k(k, diff)
            return nums[start] + k - diff[start]
        else:
            return nums[-1] + k - diff[-1]

    def find_k(self, k, diff):
        s = 0
        e = len(diff) - 1
        while s + 1 < e:
            m = s + (e - s) // 2
            if diff[m] == k:
                return m - 1
            elif diff[m] < k:
                s = m
            else:
                e = m
        return s
s = Solution2()
print(s.missingElement([4,7,9,10], 1)) #5
print(s.missingElement([4,7,9,10], 3)) #8
print(s.missingElement([1,2,4], 3))  # 6
print(s.missingElement([1,2,3,6,10,11], 5)) # 9
