from collections import deque


# class Solution(object):
#     def maze(self, ma,a):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         if len(ma) == 0:
#             return 0
#         if len(ma[0]) == 0:
#             return 0
#         m = len(ma)
#         n = len(ma[0])
#         map = {}
#         direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#
#         q = deque()
#         q.append(a)
#         map[a] = True
#         while q:
#             le = len(q)
#             for i in range(le):
#                 x, y = q.popleft()
#                 for dir in direction:
#                     if not map.has_key(((x + dir[0]), (y + dir[1]))) and ma[x + dir[0]][y + dir[1]] == 0:
#                         q.append([(x + dir[0]), (y + dir[1])])
#                         map[((x + dir[0]), (y + dir[1]))] = True
#         return count

class Solution(object):
    def __init__(self):
        self.res = False
    def maze(self, ma,a):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(ma) == 0:
            return False
        if len(ma[0]) == 0:
            return False
        if ma[a[0]][a[1]] == 1:
            return False
        map = {}
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.helper(ma,a,direction,map)
        return self.res

    def helper(self,ma,a,direction,map):
        if a[0] < 0 or a[0] >= len(ma) or a[1] < 0 or a[1] >= len(ma[0]):
            return
        if a[0] == 0 or a[0] == len(ma)-1 or a[1] == 0 or a[1] == len(ma[0]) - 1 and ma[a[0]][a[1]] == 0:
            self.res = True
            return

        for dir in direction:
            if a[0] + dir[0] > -1 and a[0] + dir[0] < len(ma) and a[1] + dir[1] > -1 and a[1] + dir[1] < len(ma[0]) and not map.has_key((a[0] + dir[0], a[1] + dir[1])) and ma[a[0] + dir[0]][a[1] + dir[1]] == 0:
                map[(a[0] + dir[0], a[1] + dir[1])] = True
                self.helper(ma, [a[0] + dir[0], a[1] + dir[1]], direction, map)
                del map[(a[0] + dir[0], a[1] + dir[1])]



if __name__ == '__main__':
    ma = [[1,1,1,1,1],
         [1,0,1,1,1],
         [1,0,0,0,1],
         [1,1,1,1,1],
         [1,1,1,1,1]]
    a = [1,1]
    s = Solution()
    print(s.maze(ma,a))
