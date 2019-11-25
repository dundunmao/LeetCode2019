class Solution:
    def canReorderDoubled(self, A):
        # build val_to_freq_hash
        val_to_freq_hash = {}
        for ele in A:
            if ele not in val_to_freq_hash:
                val_to_freq_hash[ele] = 1
            else:
                val_to_freq_hash[ele] += 1
        sorted_key = sorted(val_to_freq_hash.keys())
        for val in sorted_key:

            while val_to_freq_hash[val] > 0:
                if val * 2 in val_to_freq_hash and val_to_freq_hash[val * 2] > 0:
                    val_to_freq_hash[val] -= 1
                    val_to_freq_hash[val * 2] -= 1
                elif val % 2 == 0 and val / 2 in val_to_freq_hash and val_to_freq_hash[val / 2] > 0:
                    val_to_freq_hash[val] -= 1
                    val_to_freq_hash[val / 2] -= 1
                else:
                    break
        for val in val_to_freq_hash.values():
            if val != 0:
                return False
        return True
s = Solution()
# a = [-6,2,-6,4,-3,8,3,2,-2,6,1,-3,-4,-4,-8,4]
a = [-62,86,96,-18,43,-24,-76,13,-31,-26,-88,-13,96,-44,9,-20,-42,100,-44,-24,-36,28,-32,58,-72,20,48,-36,-45,14,24,-64,-90,-44,-16,86,-33,48,26,29,-84,10,46,50,-66,-8,-38,92,-19,43,48,-38,-22,18,-32,-48,-64,-10,-22,-48]
print(s.canReorderDoubled(a))
