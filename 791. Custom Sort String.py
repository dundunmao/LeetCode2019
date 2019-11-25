class Solution:
    def customSortString(self, S: str, T: str) -> str:
        char_to_frequency = {}
        for ele in T:
            if ele in char_to_frequency:
                char_to_frequency[ele] += 1
            else:
                char_to_frequency[ele] = 1
        res = []
        for ele in S:
            if ele in char_to_frequency:
                freq = char_to_frequency[ele]
                for e in range(freq):
                    res.append(ele)
                del char_to_frequency[ele]
        for char, freq in char_to_frequency.items():
            for i in range(freq):
                res.append(char)
        return ''.join(res)
