# class Solution:
#     def canTransform(self, start: str, end: str) -> bool:
#         n = len(start)
#         start = list(start)
#         end = list(end)
#         f = [False for i in range(n)]
#         for i in range(n):
#             if i == n - 1:
#                 if end[i] == start[i]:
#                     f[i] = True
#             elif end[i] == 'L':
#                 if start[i] == 'L':
#                     f[i] = True
#                 elif start[i] == 'X':
#                     start[i] = 'L'
#                     start[i + 1] = 'X'
#                     f[i] = True
#             elif end[i] == 'R':
#                 if start[i] == 'R':
#                     f[i] = True
#             elif end[i] == 'X':
#                 if start[i] == 'X':
#                     f[i] = True
#                 elif start[i] == 'R':
#                     start[i] = 'R'
#                     start[i + 1] = 'X'
#                     f[i] = True
#         for ele in f:
#             if ele == False:
#                 return False
#         return True
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end): return False

        A = [(s, idx) for idx, s in enumerate(start) if s == 'L' or s == 'R']
        B = [(e, idx) for idx, e in enumerate(end) if e == 'L' or e == 'R']
        if len(A) != len(B): return False

        for (s, i), (e, j) in zip(A, B):
            if s != e:
                return False
            if s == 'L':
                if i < j:
                    return False
            if s == 'R':
                if i > j:
                    return False
        return True
s = Solution()
# start = "X"
# end = "L"
# print((s.canTransform(start, end))) #f
start = "XXXXXLXXXX"
end =   "LXXXXXXXXX"
print((s.canTransform(start, end))) #T
start = "XXXLXXXXXX"
end =   "XXXLXXXXXX"
print((s.canTransform(start, end)))#T
start = "XRRXRX"
end =   "RXLRRX"
print((s.canTransform(start, end)))#F
