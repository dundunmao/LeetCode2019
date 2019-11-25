class Solution:
    def partitionLabels(self, S):
        res = []
        diff = 0
        start = 0

        char_to_freq_array = [0] * 256
        for i in range(len(S)):
            char_to_freq_array[ord(S[i])] += 1

        char_to_freq_array_new = [0] * 256
        for i in range(len(S)):
            if char_to_freq_array_new[ord(S[i])] > 0:
                diff -= 1
            else:
                diff += char_to_freq_array[ord(S[i])]
                char_to_freq_array_new[ord(S[i])] += 1
                diff -= 1
            if diff == 0:
                res.append(i - start + 1)
                start = i + 1
        return res
class Solution2:
    def partitionLabels(self, S):
        res = []
        start = 0
        n = len(S)
        char_array = []
        start_end_hash = {}
        # 往start_end_hash里存{char:freq}
        # 往char_array里存char，无duplicate的按出现顺序的char的list
        for i in range(n):
            cur = S[i]
            if cur not in start_end_hash:
                start_end_hash[cur] = [i, i]
                char_array.append(cur)
            else:
                start_end_hash[cur][1] = i
        # 找到每一块的边，更新res
        maxi = start_end_hash[char_array[0]][1]
        for i in range(1, len(char_array)):
            if start_end_hash[char_array[i]][0] > maxi:
                res.append(maxi - start + 1)
                start = maxi + 1
            maxi = max(maxi, start_end_hash[char_array[i]][1])
        res.append(maxi - start + 1)
        return res

s=Solution2()
x = "ababcbacadefegdehijhklij" #[9,7,8]
print(s.partitionLabels(x))
x = "caedbdedda" #[1,9]
print(s.partitionLabels(x))
