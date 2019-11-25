class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        max_x = float('-inf')
        min_x = float('inf')
        y_hash = {}
        for ele in points:
            max_x = max(max_x, ele[0])
            min_x = min(min_x, ele[0])
            if ele[1] in y_hash and ele[0] not in y_hash[ele[1]]:
                y_hash[ele[1]].append(ele[0])
            elif ele[1] not in y_hash:
                y_hash[ele[1]] = [ele[0]]
        y_mid_line = (max_x + min_x) / 2

        for ele in y_hash.values():
            if sum(ele) / len(ele) != y_mid_line:
                return False
        return True



s = Solution()
p = [[0,0],[1,0],[3,0]] #F
print(s.isReflected(p))
p = [[-16,1],[16,1],[16,1]] #T
print(s.isReflected(p))
p = [[1,1],[-1,1]] # t
print(s.isReflected(p))
p = [[1,1],[-1,-1]] # f
print(s.isReflected(p))
