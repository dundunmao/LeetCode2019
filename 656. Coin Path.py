class Solution:
    def cheapestJump(self, A, B):
        all_results = [None] * len(A)
        index = 0
        max_units = B
        dag_result = self.dfs(A, index, max_units, all_results)
        res = []
        if not dag_result.has_solution:
            return res
        res.append(1)
        i = 0
        while i != len(A) - 1:
            res.append(all_results[i].next_index + 1)
            i = all_results[i].next_index
        return res

    def dfs(self, A, index, max_units, all_results):
        # special case
        if A[index] == -1:
            return Result(False, 0, 0)
        if index == len(A) - 1:
            return Result(True, A[index], index)
        if all_results[index] != None:
            return all_results[index]

        has_solution = False
        min_cost = float('inf')
        next_index = len(A)

        for i in range(index + 1, min(index + max_units + 1, len(A))):
            child_res = self.dfs(A, i, max_units, all_results)
            if child_res.has_solution and (not has_solution or min_cost > A[i] + child_res.min_cost):
                has_solution = True
                min_cost = A[i] + child_res.min_cost
                next_index = i

        result = Result(has_solution, min_cost, next_index)
        all_results[index] = result

        return result



class Result:
    def __init__(self, has_solution, min_cost, next_index):
        self.has_solution = has_solution
        self.min_cost = min_cost
        self.next_index = next_index

class Solution1:
    def cheapestJump(self, A, B):
        all_results = [None for i in range(len(A))]
        self.dfs(0, A, B, all_results)
        i = 0
        res = [1]
        while i < len(A) - 1:
            res.append(all_results[i][2] + 1)
            i = all_results[i][2]
        return res

    def dfs(self, pos, A, B, all_results):
        if A[pos] == -1:
            return (False, 0, 0)
        if all_results[pos]:
            return all_results[pos]
        if pos == len(A) - 1:
            all_results[pos] = (True, A[-1], pos)
            return all_results[pos]
        if pos >= len(A):
            return

        else:
            res = float('inf')
            index = len(A)
            if_result = False
            for i in range(1, B + 1):
                if pos + i < len(A):
                    cur = self.dfs(pos + i, A, B, all_results)
                    if cur[0] and (not if_result or cur[1] + A[pos] < res):
                        res = cur[1] + A[pos]
                        index = pos + i
                        if_result = True

        all_results[pos] = (if_result, res, index)
        return all_results[pos]

s = Solution1()
# A = [1,2,4,-1,2]
# B = 2
# print((s.cheapestJump(A, B)))
A = [1,2,4,-1,2]
B = 1
print((s.cheapestJump(A, B)))

