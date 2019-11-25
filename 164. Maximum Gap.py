import math
class Solution:
    def maximumGap(self, nums) -> int:
        n = len(nums)
        if len(nums) < 2:
            return 0
        max_value = max(nums)
        min_value = min(nums)
        bucket_capacity = math.ceil((max_value - min_value) / (len(nums) - 1))
        max_bucket = [float('-inf') for i in range(n)]
        min_bucket = [float('inf') for i in range(n)]
        for i in range(0, len(nums)):
            if nums[i] == min_value or nums[i] == max_value:
                continue
            bucket_id = (nums[i] - min_value) // bucket_capacity
            print(bucket_id, nums[i])
            max_bucket[bucket_id] = max(max_bucket[bucket_id], nums[i])
            min_bucket[bucket_id] = min(min_bucket[bucket_id], nums[i])
        res = 0
        start = min_value
        for i in range(n):
            if min_bucket[i] == float('inf') and max_bucket[i] == float('-inf'):
                continue
            res = max(res, min_bucket[i] - start)
            start = max_bucket[i]
        res = max(res, max_value - start)

        return res

s = Solution()
x = [3,6,9,13,15,17]
print(s.maximumGap(x))

x = [3,6,9,1]
print(s.maximumGap(x))
x = [20]
print(s.maximumGap(x))
x = [1,1,1,1]
print(s.maximumGap(x))
x = [12115,10639,2351,29639,31300,11245,16323,24899,8043,4076,17583,15872,19443,12887,5286,6836,31052,25648,17584,24599,13787,24727,12414,5098,26096,23020,25338,28472,4345,25144,27939,10716,3830,13001,7960,8003,10797,5917,22386,12403,2335,32514,23767,1868,29882,31738,30157,7950,20176,11748,13003,13852,19656,25305,7830,3328,19092,28245,18635,5806,18915,31639,24247,32269,29079,24394,18031,9395,8569,11364,28701,32496,28203,4175,20889,28943,6495,14919,16441,4568,23111,20995,7401,30298,2636,16791,1662,27367,2563,22169,1607,15711,29277,32386,27365,31922,26142,8792]
print(s.maximumGap(x))
x = [15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]
print(s.maximumGap(x))
