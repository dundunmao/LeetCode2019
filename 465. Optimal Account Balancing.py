class Solution:
    def minTransfers(self, transactions) -> int:
        value_hash = {}
        for ele in transactions:
            if ele[0] not in value_hash:
                value_hash[ele[0]] = ele[2]
            else:
                value_hash[ele[0]] += ele[2]
            if ele[1] not in value_hash:
                value_hash[ele[1]] = -ele[2]
            else:
                value_hash[ele[1]] -= ele[2]
        value_list = []
        for ele in value_hash.values():
            if ele != 0:
                value_list.append(ele)
        return self.dfs(0, value_list)

    def dfs(self, pos, value_list):
        if pos == len(value_list):
            return 0
        cur = value_list[pos]
        if cur == 0:
            return self.dfs(pos + 1, value_list)
        res = float('inf')
        for i in range(pos + 1, len(value_list)):
            next = value_list[i]
            if cur * next < 0:
                value_list[i] = cur + next
                res = min(res, 1 + self.dfs(pos + 1, value_list))
                value_list[i] = next
                if cur + next == 0:
                    break
        return res
s = Solution()
a = [[0,1,10], [2,0,5]]
print((s.minTransfers(a))
      )
