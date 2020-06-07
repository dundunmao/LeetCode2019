class Solution:
    def sortString(self, s: str) -> str:
        cnt, ans, asc = collections.Counter(s), [], True
        while cnt:            # if Counter not empty.
            # traverse keys in ascending/descending order.
            for c in sorted(cnt.keys()) if asc else reversed(sorted(cnt.keys())):
                ans.append(c)    # append the key.
                cnt[c] -= 1       # decrease the count.
                if cnt[c] == 0:       # if the count reaches to 0.
                    del cnt[c]     # remove the key from the Counter.
            asc ^= True              # change the order.
        return ''.join(ans)        