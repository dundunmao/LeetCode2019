# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:

from collections import Counter


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash = Counter(s)
        # hash = {'e':2,'d':1}
        temp = sorted(hash.items(), key=lambda x: x[1], reverse=True)
        res = []
        for k, v in temp:
            for i in range(v):
                res.append(k)
        return ''.join(res)
################
class Solution1:
    def frequencySort(self, s: str) -> str:
        char_to_freq_hash = {}
        for ele in s:
            if ele in char_to_freq_hash:
                char_to_freq_hash[ele] += 1
            else:
                char_to_freq_hash[ele] = 1
        temp = sorted(char_to_freq_hash.items(), key=lambda  x: x[1], reverse=True)
        # res = []
        # for k, v in temp:
        #     for i in range(v):
        #         res.append(k)
        # return ''.join(res)
        return ''.join([char * freq for char, freq in temp])

if __name__ == "__main__":
    a = "tree"
    b = "AATTCCGG"
    c = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]

    s = Solution1()
    print(s.frequencySort(a))
