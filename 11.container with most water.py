class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            res = max(min(height[left],height[right])*(right-left),res)
            if height[left] < height[right]:
                left+=1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return res