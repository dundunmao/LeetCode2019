
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        path = []
        res = []
        pos = 0
        candidates.sort()
        sum_up = 0
        self.helper(candidates, target, res, path, pos, sum_up)
        return res

    def helper(self, candidates, target, res, path, pos, sum_up):
        if sum_up == target:
            res.append(path[:])
            return
        if sum_up > target:
            return
        for i in range(pos, len(candidates)):
            path.append(candidates[i])
            self.helper(candidates, target, res, path, i, sum_up + candidates[i])
            path.pop()

            #把 i 这个值从sum_up减掉


if __name__ == '__main__':
    candidates = [2,6,7] #[[7],[2, 2, 3]]
    candidates2 = [8, 7, 4, 3]  #[[3, 4, 4], [3, 8], [4, 7]]
    target = 7
    target2 = 11
    s = Solution()
    print(s.combinationSum(candidates2, target2))


