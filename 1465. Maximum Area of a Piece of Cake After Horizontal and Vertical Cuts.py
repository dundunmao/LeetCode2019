class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        # horizontal
        hor_array = [0]
        horizontalCuts.sort()
        for ele in horizontalCuts:
            hor_array.append(ele)
        hor_array.append(h)
        max_range_hor = 0
        for i in range(1, len(hor_array)):
            max_range_hor = max(max_range_hor, hor_array[i] - hor_array[i - 1])

        # vertical
        ver_array = [0]
        verticalCuts.sort()
        for ele in verticalCuts:
            ver_array.append(ele)
        ver_array.append(w)
        max_range_ver = 0
        for i in range(1, len(ver_array)):
            max_range_ver = max(max_range_ver, ver_array[i] - ver_array[i - 1])
        return (max_range_hor * max_range_ver) % (10 ** 9 + 7)
