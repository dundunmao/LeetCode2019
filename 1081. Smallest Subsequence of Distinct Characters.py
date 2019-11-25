class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last_pos_hash = {}
        for i in range(len(text)):
            last_pos_hash[text[i]] = i
        length = len(last_pos_hash)
        res = []
        exist_set = set()
        for i in range(len(text)):
            if len(res) == 0:
                res.append(text[i])
                exist_set.add(text[i])
            else:
                while len(res) > 0 and res[-1] > text[i] and last_pos_hash[res[-1]] > i and text[i] not in exist_set:
                    cur = res.pop()
                    exist_set.remove(cur)
                if text[i] not in exist_set:
                    res.append(text[i])
                    exist_set.add(text[i])
        return ''.join(res)
s = Solution()
print(s.smallestSubsequence("ecbacba"))
