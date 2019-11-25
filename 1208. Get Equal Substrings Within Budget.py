class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        diff_array = []
        #算出对应字母的distance 分别是多少
        for i in range(len(s)):
            diff_array.append(abs(ord(s[i]) - ord(t[i])))
        i = 0
        j = 0
        sum_up = 0
        maxi = 0
        # 两个指针，找subarray sum <= maxCost
        while j < len(s):
            # print(i,j)
            sum_up += diff_array[j]
            if sum_up <= maxCost:
                maxi = max(maxi, j - i + 1)

            else:
                while sum_up > maxCost and i <= j:
                    sum_up -= diff_array[i]
                    i += 1
            j += 1
        return maxi
