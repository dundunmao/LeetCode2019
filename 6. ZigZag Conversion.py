class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = [[] for i in range(numRows)]
        temp = []
        i = 0
        while i < len(s):
            for idx in range(0,numRows):   #从上到下
                if i < len(s):
                    res[idx].append(s[i])
                    i += 1
            for idx in range(numRows-2,0,-1):  #从下到上
                if i < len(s):
                    res[idx].append(s[i])
                    i += 1
        for idx in range(0,len(res)):   #合并
            temp.append(''.join(res[idx]))
        return ''.join(temp)

if __name__ == "__main__":
    x = Solution()
    s = "PAYPALISHIRING"
    n = 4
    print x.convert(s,n)