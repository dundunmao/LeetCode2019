# python 2
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, num):
        num = [str(x) for x in num]
        num.sort(cmp=lambda o1, o2 : cmp(o2 + o1, o1 + o2))  #把nums里两两比较，按o2 + o1小，就o1在前
        if num[0] == '0':
            return '0'
        return ''.join(num)

# python 3
import functools


class Solution:
    def largestNumber(self, num):
        num = [str(ele) for ele in num]
        res = sorted(num, key=functools.cmp_to_key(self.cmp_fuc))
        if res[0] == '0':
            return '0'
        return ''.join(res)

    def cmp_fuc(self, o1, o2):
        return int(o2 + o1) - int(o1 + o2)


class Solution1:
    def largestNumber(self, nums) -> str:
        res = []
        res.append(str(nums[0]))
        for i in range(1, len(nums)):
            j = float('inf')
            for j in range(len(res)):
                if res[j] + str(nums[i]) < str(nums[i]) + res[j]:
                    res.insert(j, str(nums[i]))
                    break
            if j == len(res) - 1:
                res.append(str(nums[i]))
        if res[0] == '0':
            return '0'
        return ''.join(res)

s = Solution2()
a = [3,30,34,5,9]
print(s.largestNumber(a))
