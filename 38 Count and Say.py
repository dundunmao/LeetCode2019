
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur = [1]
        while n != 1:
            cur = self.count(cur)
            n -= 1
        ans = [str(ele) for ele in cur]
        return ''.join(ans)
    def count(self,s):

        hash = {}
        array = []
        count = 1
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                array.append(count)
                array.append(s[i-1])
                count = 1
            else:
                count += 1
        array.append(count)
        array.append(s[-1])
        # return ''.join(array)
        return array

class Solution1(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        res = list(str(1))
        for i in range(2,n+1):
            res = self.pattern(res)
            print res
        return ''.join(res)
    def pattern(self,res):
        ans = []
        i = 0
        while i < len(res):
            j = i+1
            count = 1
            while j < len(res) and res[j] == res[j-1]:
                count += 1
                j+=1
            ans += [str(count),res[i]]
            print(ans)
            i = j
        return ans


#####################
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'

        for i in range(2, n + 1):
            cur = ''
            count = 1
            for j in range(1, len(res)):
                if res[j] == res[j - 1]:
                    count += 1
                else:
                    cur += str(count)
                    cur += res[j - 1]
                    count = 1
            cur += str(count)
            cur += res[-1]
            res = cur
        return res


if __name__ == '__main__':
    s = Solution1()
    n = 1
    print s.countAndSay(n)
