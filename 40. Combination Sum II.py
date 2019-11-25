class Solution:
    def combinationSum2(self, candidates, target):
        path = []
        res = []
        pos = 0
        candidates.sort()
        sum_up=0
        self.helper(candidates,target,res,path,pos,sum_up)
        return res
    def helper(self,candidates,target,res,path,pos,sum_up):
        if sum_up == target:
            res.append(path[:])
            return
        if sum_up > target:
            return
        for i in range(pos,len(candidates)):
            if i != pos and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            sum_up+= candidates[i]
            self.helper(candidates,target,res,path,i+1,sum_up)
            sum_up-=path[-1]
            path.pop()
if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5] #[[1, 7],[1, 2, 5],[2, 6],[1, 1, 6]]
    # candidates2 =  [8, 7, 4, 3]  #[[3, 4, 4], [3, 8], [4, 7]]
    target = 8
    target2 = 11
    s = Solution()
    print(s.combinationSum2(candidates, target))
