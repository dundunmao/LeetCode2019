class Solution:
    def numSmallerByFrequency(self, queries, words):
        res_q = []
        res_w = []
        res = []
        for ele in queries:
            res_q.append(self.helper(ele))
        for ele in words:
            res_w.append(self.helper(ele))
        res_w.sort()
        for ele in res_q:
            start = 0
            end = len(res_w) - 1
            while start + 1 < end:
                mid = start + (end - start) // 2
                if res_w[mid] <= ele:
                    start = mid
                else:
                    end = mid
            if res_w[end] > ele:
                res.append(len(res_w) - end)
        return res


    def helper(self, string):
        n = len(string)
        a = [0 for i in range(26)]
        for i in range(len(string)):
            a[ord(string[i]) - 97] += 1
        for i in range(26):
            if a[i] != 0:
                return a[i]

s = Solution()
q = ["cbd"]
w =["zaaaz"]
print(s.numSmallerByFrequency(q, w))



q = ["bbb","cc"]
w =["a","aa","aaa","aaaa"]
print(s.numSmallerByFrequency(q, w))
