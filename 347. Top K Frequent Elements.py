from collections import Counter
from heapq import *
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        hash = Counter(nums)  #用hash算频次
        # 变成（频次，element）这样的数组，这样方便放入heap，这里count放的是负的，因为heapq是mini heap
        hash_count = [(-count,num) for (num,count) in hash.items()]
        q = []
        for i in range(len(hash)):  #都塞入heap
            heappush(q, hash_count[i])
        for j in range(k):      #pop出来k个
            res.append(heappop(q)[1])
        return res


from collections import Counter
from heapq import *


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        hash = Counter(nums)
        hash_count = [(count, num) for (num, count) in hash.items()]
        q = []
        for i in range(k):
            heappush(q, hash_count[i])
        for j in range(k, len(hash_count)):
            if q[0][0] < hash_count[j][0]:
                heappop(q)
                heappush(q, hash_count[j])
        return [item[1] for item in q]

from collections import Counter
class Solution3(object):
    def topKFrequent(self, nums, k):
        bucket = [[] for i in range(len(nums)+1)] #建立桶的array
        hash = Counter(nums)  #把每个num的frequency算出来
        for key,val in hash.items(): #把frequency作为index,把num装桶里
            bucket[val].append(key)
        res = []
        for j in range(len(bucket) - 1, -1, -1): #从后往前，找出桶里不空的k个桶
            if len(res) < k and bucket[j] != []:
                res += bucket[j]
        return res




if __name__ == "__main__":
    words = [1,1,1,2,2,3]
    x = Solution3()
    print x.topKFrequent(words,2)
