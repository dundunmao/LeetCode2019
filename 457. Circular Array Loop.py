class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        all_results = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            # cur = Result(index)
            visit_round = i + 1
            if self.dfs(i, all_results, nums, visit_round):
                return True
        return False

    # dfs的意思是给个起点，看能不能返回起点且步长大于1，是就return True
    def dfs(self, index, all_results, nums, visit_round):
        # 走到过，没重合
        if all_results[index] > 0 and all_results[index] != visit_round:
            return False

        next_index = self.get_next(index, nums)
        # 方向不对
        if nums[index] * nums[next_index] < 0:
            return False
        # 步长不大于1
        if index == next_index:
            all_results[index] = visit_round
            return False
        if all_results[next_index] == visit_round:
            return True
        all_results[index] = visit_round
        return self.dfs(next_index, all_results, nums, visit_round)

    def get_next(self, index, nums):
        next_index = index + nums[index]
        if next_index >= 0:
            return (next_index) % len(nums)
        else:
            return (next_index + ((-next_index // len(nums)) + 1) * len(nums)) % len(nums)


# def building(a):
#     stack = []
#     stack.append(0)
#     for i in range(1, len(a)):
#         while stack and a[i] > a[stack[-1]]:
#             stack.pop()
#         stack.append(i)
#     res = []
#     start = 0
#     for ele in stack:
#         res = res + [a[ele]] * (ele - start)
#         res.append(-1)
#         start = ele + 1
#     return res
# print(building([1,2,3,4]))  # [6, 6, 6, 6, 6, -1, -1]
# print(building([1,2,5,4,1,6,4, 5]))  #[6, 6, 6, 6, 6, -1, 5, -1]



s = Solution()
a = [2, -1, 1, 2, 2]
# print(s.get_next(2,a))
print(s.circularArrayLoop(a))
a = [-1,-1,-3]
print(s.get_next(2,a))
print(s.circularArrayLoop(a))
a = [-1,2]
print(s.get_next(2,a))
print(s.circularArrayLoop(a))

