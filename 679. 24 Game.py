class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        ops = ['+', '-', '*', '/']
        return self.dfs(nums, ops)

    def dfs(self, nums, ops):
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                new = []
                for k in range(len(nums)):
                    if k != i and k != j:
                        new.append(nums[k])

                a = nums[i]
                b = nums[j]
                for ele in ops:
                    if (ele == '+' or ele == '*') and j > i:
                        continue
                    if ele == '+':
                        new.append(a + b)
                    elif ele == '-':
                        new.append(a - b)
                    elif ele == '*':
                        new.append(a * b)
                    elif ele == '/':
                        if b != 0:
                            new.append(a / b)
                        else:
                            continue
                    if self.dfs(new, ops):
                        return True
                    new.pop()

