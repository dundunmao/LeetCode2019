#给定正整数数组nums，计算其中不想交的3段子数组的最大和。每段子数组的长度为k。
# # Example:
#
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        k_size = [0] * n
        sum = 0
        # 算出k size的subarray sum
        for i in range(n):
            if i >= k:
                sum -= nums[i - k]
            sum += nums[i]
            if i >= k - 1:
                k_size[i - k + 1] = sum
        # 算出每个位置的从左到当前的最大subarray sum
        left = [0] * n
        maxi_index = 0
        for i in range(n):
            if k_size[i] > k_size[maxi_index]:
                maxi_index = i
            left[i] = maxi_index
        # 算出每个位置的从右到当前的最大subarray sum
        right = [0] * n
        maxi_index = n - 1
        for i in range(n - 1, -1, -1):
            if k_size[i] >= k_size[maxi_index]:
                maxi_index = i
            right[i] = maxi_index
        #中间的subarray，从k开始取，一直取到n-k，算三个subarray的总和
        res_value = float('-inf')
        res = [0, k, k + k]
        for i in range(k, n - k):
            if res_value < k_size[left[i - k]] + k_size[i] + k_size[right[i + k]]:
                res[0], res[1], res[2] = left[i - k], i, right[i + k]
                res_value = k_size[left[i - k]] + k_size[i] + k_size[right[i + k]]
        return res


class Solution1:
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        # k_size_subarray_sum
        k_size_subarray_sum = [0] * n
        pre_sum = 0
        start = 0
        for i in range(0, n):
            pre_sum += nums[i]
            if i - start + 1 == k:
                k_size_subarray_sum[start] = pre_sum
                pre_sum -= nums[start]
                start += 1

        # left_max_index
        left_max = [0] * n
        max_sum = k_size_subarray_sum[0]
        for i in range(1, n):
            if k_size_subarray_sum[i] > max_sum:
                max_sum = k_size_subarray_sum[i]
                left_max[i] = i
            else:
                left_max[i] = left_max[i - 1]

        # right_max
        right_max = [0] * n
        max_sum = k_size_subarray_sum[-k]
        right_max[-k] = n - k
        for i in range(n - k - 1, -1, -1):
            if k_size_subarray_sum[i] > max_sum:
                max_sum = k_size_subarray_sum[i]
                right_max[i] = i
            else:
                right_max[i] = right_max[i + 1]
            # result
        maxi = float('-inf')
        res = []
        for i in range(k, n):
            if i + 1 + k < n:
                cur = k_size_subarray_sum[left_max[i - k]] + k_size_subarray_sum[i] + k_size_subarray_sum[right_max[i + k]]
                if maxi < cur:
                    res = [left_max[i - k], i, right_max[i + k]]
                    maxi = cur
        return res

if __name__ == "__main__":

    x = Solution1()
    s = [1,2,1,2,6,7,5,1]
    p = 2
    print(x.maxSumOfThreeSubarrays(s,p)) # [0, 3, 5]

    s = [1,2,1,2,6,1,1,7,5,1]
    p = 2
    print(x.maxSumOfThreeSubarrays(s,p)) # [0, 3, 7]

