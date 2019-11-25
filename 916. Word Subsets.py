class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        res = []
        # 把B里的所有word合进几个map里，每个char取他在各个word里最大的那个freq
        char_to_freq_b = [0] * 26
        for word in B:
            sub_char_to_freq_b = [0] * 26
            for char in word:
                sub_char_to_freq_b[ord(char) - 97] += 1
            for i in range(26):
                if sub_char_to_freq_b[i] > char_to_freq_b[i]:
                    char_to_freq_b[i] = sub_char_to_freq_b[i]
        # 遍历每个word, 放入map，跟B的map对比相应位置,map_B里的需要小于map_A里的
        for word in A:
            flag = True
            char_to_freq_a = [0] * 26
            # get map of word in A
            for char in word:
                char_to_freq_a[ord(char) - 97] += 1
            for i in range(26):
                if char_to_freq_b[i] > 0 and char_to_freq_a[i] < char_to_freq_b[i]: #只找B里有的
                    flag = False
                    break
            if flag == False:
                continue
            res.append(word)

        return res

if __name__ == '__main__':
    s = Solution()
    a = ["amazon","apple","facebook","google","leetcode"]
    b = ["e","o"]
    print(s.wordSubsets(a,b))
