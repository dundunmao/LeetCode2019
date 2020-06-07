class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjance_list = {}
        res = []
        memo = {}
        for ele in prerequisites:
            if ele[0] in adjance_list:
                adjance_list[ele[0]].append(ele[1])
            else:
                adjance_list[ele[0]] = [ele[1]]
        for ele in queries:
            res.append(self.dfs(ele[0], ele[1], adjance_list, memo))

        return res

    def dfs(self, s, e, adjance_list, memo):
        if (s, e) in memo:
            return memo[(s, e)]

        elif s not in adjance_list:
            memo[(s, e)] = False
            return False

        else:
            for ele in adjance_list[s]:
                if ele == e:
                    memo[(s, e)] = True
                    return True
                else:
                    res = self.dfs(ele, e, adjance_list, memo)
                if res == True:
                    memo[(s, e)] = True
                    return True
        memo[(s, e)] = False
        return False



