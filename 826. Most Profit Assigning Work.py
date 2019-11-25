class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # sort worker
        worker.sort()
        jobs = []
        for p, d in zip(profit, difficulty):
            jobs.append(Job(d, p))
        # 按diff 来 sort job
        jobs.sort()
        maxi_profit = float('-inf')
        # 把 job里的profit更新成 比它小的diff里profit最大的
        for job in jobs:
            maxi_profit = max(maxi_profit, job.profit)
            job.profit = maxi_profit
        j = 0
        res = 0
        # 从小worker开始，找小worker最近diff
        for w in worker:
            while j < len(jobs) and jobs[j].diff <= w:
                j += 1
            if j - 1 < 0:
                continue
            res += jobs[j - 1].profit
        return res


class Job:
    def __init__(self, diff, profit):
        self.diff = diff
        self.profit = profit

    def __lt__(a, b):
        return a.diff < b.diff
