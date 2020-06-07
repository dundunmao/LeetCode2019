class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        char_to_freq_hash = {}
        for ele in arr1:
            if ele in char_to_freq_hash:
                char_to_freq_hash[ele] += 1
            else:
                char_to_freq_hash[ele] = 1

        for ele in arr2:
            for i in range(char_to_freq_hash[ele]):
                res.append(ele)
            del char_to_freq_hash[ele]
        temp = sorted(char_to_freq_hash.keys())
        for ele in temp:
            for i in range(char_to_freq_hash[ele]):
                res.append(ele)
        return res
