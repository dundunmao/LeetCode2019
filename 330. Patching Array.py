class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        i = 0
        end = 0 # 0~total已经符合条件，total是符合条件的右边界
        ans = 0
        size = len(nums)
        while end < n:
            if i < size and nums[i] <= end + 1 : #判断右边界能不能到nums[i]
                end += nums[i]  #重新定义右边界
                i += 1
            else:
                end += end + 1 #如果到了右边界就乘2
                ans += 1 #说明需要加一个数
        return ans


class Solution2(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        i = 0
        end = 0 # 0~end已经符合条件，end是符合条件的右边界
        res = 0
        size = len(nums)
        while end+1 <= n:
            candidate = end+1  # 潜在要加的数
            # 三种情况需要加一个数：
            # 1：nums本身是空的
            # 2：nums里的数都用完了
            # 3：当前的数比要加的数大
            if nums == [] or i >= size or (i < size and nums[i] > candidate): #需要加add这个数
                res += 1 #所以结果要➕一
                end += candidate #end要往后扩到+=add的位置
            # 下面情况是不需要加数，但是end要往后扩
            else:
                # 这种情况是end没到n，当前数比要加的数小
                while candidate <= n and i < size and nums[i] <= candidate:
                    end += nums[i]
                    i += 1
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [1,5,10]
    n = 20  #2
    # print s.minPatches(nums, n)
    # nums = [1,2,2]
    # n = 5 #0
    # print s.minPatches(nums, n)
    # nums = []
    # n = 7 #3
    # print s.minPatches(nums, n)
    # nums =[1, 2, 31, 33]
    # n = 2147483647 #28
    # print s.minPatches(nums, n)
    # nums =[1,3]
    # n = 6 #1
    print s.minPatches(nums, n)
