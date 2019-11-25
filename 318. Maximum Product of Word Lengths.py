class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        n = len(words)
        bytes = [0 for i in range(n)]  #存每个word的bit码
        for i in range(n):
            val = 0
            # 把每个word的bit码算出来，
            # 一共26位，哪个字母存在，哪个位上就是1
            for j in range(len(words[i])):
                val |= 1 << (ord(words[i][j])-ord('a'))
            bytes[i] = val
        # 暴力查每两个word,只要没有相同char，就求一下乘积
        for i in range(n):
            for j in range(i+1, n):
                if bytes[i] & bytes[j] == 0: #如果两个word的bit码并上为0，说明没有相同char
                    res = max(res,len(words[i]*len(words[j])))  #这时就算一下乘积
        return res
if __name__ == "__main__":
    words =  ["abcw","baz","foo","bar","xtfn","abcdef"]
    x = Solution()
    print x.maxProduct(words)
