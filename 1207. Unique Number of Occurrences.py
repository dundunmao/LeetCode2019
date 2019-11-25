class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hash = {}
        for ele in arr:
            if ele in hash:
                hash[ele] += 1
            else:
                hash[ele] = 1
        hash_fre = {}
        for ele in hash.values():
            if ele in hash_fre:
                return False
            else:
                hash_fre[ele] = 1
        return True
