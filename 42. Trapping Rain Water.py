# heap方法
class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if len(heights) == 0:
            return 0
        max_heights = []
        max_heights.append(0)
        for i in range(len(heights)):
            max_heights.append(max(max_heights[i],heights[i]))
        maxi = 0
        area = 0
        for i in range(len(heights)-1,-1,-1):
            if min(maxi, max_heights[i]) > heights[i]:
                area += min(maxi, max_heights[i]) - heights[i]
            maxi = max(maxi,heights[i])
        return area

# 4two_pointer
class Solution1:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        left = 0
        right = len(heights)-1
        result = 0
        if left >= right:
            return result
        left_height = heights[left]
        right_height = heights[right]
        while left < right:
            if left_height < right_height:
                left += 1
                if left_height > heights[left]:
                    result += left_height - heights[left]
                else:
                    left_height = heights[left]
            else:
                right -= 1
                if right_height > heights[right]:
                    result += right_height - heights[right]
                else:
                    right_height = heights[right]
        return result
# 单调栈
class Solution:
    def trap(self, a: List[int]) -> int:
        n = len(a)
        if n == 0:
            return 0
        # water_stack.append(0)
        res = 0
        # left
        pivot = 0
        i = 1
        while i < n:
            temp = 0
            while i < n and a[i] < a[pivot]:
                temp += a[i]
                i += 1
            if i == n:
                break
            res += min(a[pivot], a[i]) * (i - pivot - 1) - temp
            pivot = i
            i += 1
        # right
        pivot = n - 1
        j = n - 2
        while j >= 0:
            temp = 0
            while j >= 0 and a[j] <= a[pivot]:
                temp += a[j]
                j -= 1
            if j == -1:
                break
            res += min(a[pivot], a[j]) * (pivot - j - 1) - temp
            pivot = j
            j -= 1
        return res


class Solution3:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        # left
        left_max = [0] * n
        # base case
        left_max[0] = height[0]
        # general case
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        # right
        right_max = [0] * n
        # base case
        right_max[n - 1] = height[n - 1]
        # general case
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        # result
        res = 0
        for i in range(1, n - 1):
            min_of_two_side_max = min(left_max[i], right_max[i])
            res += min_of_two_side_max - height[i]
        return res

# 316. Remove Duplicate Letters


if __name__ == "__main__":
    a = [0,1,0,2,1,0,1,3,2,1,2,1]
    # s = Solution3()
    # print(s.trapRainWater(a))
    s = Solution3()
    print(s.trap(a))
