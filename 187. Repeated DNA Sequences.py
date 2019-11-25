class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        hash = set() #key出现过没
        double_words = set() #在结果里有没有过
        res = []
        encode = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        for i in range(0,len(s)-9):
            v = 0
            for j in range(i,i+10): #把ACGT变成2进制排放在一起
                v <<=2  #因为是四个字母，所以是2^2所以每次左移2位
                v |= encode[s[j]]
            if v not in hash:
                hash.add(v)
            elif (v in hash) and v not in double_words:
                double_words.add(v)
                res.append(s[i:i+10])
        return res


#rolling hash
# 这个以2位底的有会出现不同string同一个key的情况，所以是错误的
class Solution1(object):
    def findRepeatedDnaSequences(self, s):
        if len(s) <= 10:
            return []
        encode= {'A':0,'C':1,'G':2,'T':3}
        hash_res= {}
        res = set()
        j = 2**9
        temp = 0
        for i in range(0,10):
            temp += j * encode[s[i]]
            j >>= 1
        hash_res[temp] = True
        start = 0
        for i in range(10,len(s)):
            temp -= 2**9 * encode[s[start]]
            temp *= 2
            temp += encode[s[i]]
            start += 1
            if temp in hash_res:
                res.add(s[start:i+1])
            else:
                hash_res[temp] = start
        return list(res)
# 这个是最终的，要以4为底
class Solution2(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        encode= {'A':1,'C':2,'G':3,'T':4}
        hash_res= {}
        res = set()
        j = 4**10
        temp = 0
        for i in range(0,10):
            temp += j * encode[s[i]]
            j >>= 2
        hash_res[temp] = True
        j = 0
        for i in range(10,len(s)):
            temp -= 4**10 * encode[s[j]]
            temp *= 4
            temp += 4 * encode[s[i]]
            j += 1
            if temp in hash_res:
                res.add(s[j:i+1])
            else:
                hash_res[temp] = True
        return list(res)

if __name__ == '__main__':
    s = Solution()

    X = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print s.findRepeatedDnaSequences(X)
    X = "ACCCTCCCACTTGGATGCCGCACGTGTCGACTAACCTTACATTGTCCCCCCACCTCCAGACGGTTAACTCTTGAAATGGGGGAATAGCTGCTTGCGCGTG"
    print s.findRepeatedDnaSequences(X)
