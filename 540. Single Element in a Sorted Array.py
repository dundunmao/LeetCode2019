class Solution:
    def singleNonDuplicate(self, nums) -> int:
        start = 0
        end = len(nums)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid % 2 == 0:
                if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                    start = mid
                elif mid + 1 < len(nums) and nums[mid] != nums[mid + 1]:
                    end = mid
                else:
                    break
            else:
                if mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                    start = mid
                elif mid - 1 >= 0 and nums[mid] != nums[mid - 1]:
                    end = mid
                else:
                    break
        if start % 2 == 0:
            return nums[start]
        else:
            return nums[end]


class Solution:
    def singleNonDuplicate(self, nums) -> int:
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    start = mid

                else:
                    end = mid
            else:
                if mid - 1 >= 0 and nums[mid] == nums[mid - 1]:
                    start = mid

                else:
                    end = mid
        if start % 2 == 0:
            return nums[start]
        else:
            return nums[end]
s = Solution()
a = [1,1,2]
print(s.singleNonDuplicate(a))
