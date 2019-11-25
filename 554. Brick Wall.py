class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        hash_table = {}
        for i in range(len(wall)):
            temp = 0
            for j in range(0, len(wall[i]) - 1):
                temp += wall[i][j]
                if temp in hash_table:
                    hash_table[temp] += 1
                else:
                    hash_table[temp] = 1

        max_value = 0   # 开始没附初值，而是直接求max(hash_table.values())，没考虑hash_table.values()==[]的情况 [[1],[1],[1]]
        if len(hash_table.values()) != 0:
            max_value = max(hash_table.values())
        return len(wall) - max_value
