# 给一组词，问里面哪些词在键盘的同一行里
# 例子：input=["Hello","Alaska","Dad","Peace"]，output = ['Alaska', 'Dad']
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        ans = []
        f = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        s = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        t = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        for w in words:
            w_l = w.lower()
            tran = []
            count = 0
            if w_l[0] in f:
                tran = f
            if w_l[0] in s:
                tran = s
            if w_l[0] in t:
                tran = t
            for l in w_l:
                if l in tran:
                    count += 1
            if count == len(w):
                ans.append(w)
        return ans
class Solution_leet(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a=set('qwertyuiop')
        b=set('asdfghjkl')
        c=set('zxcvbnm')
        ans = []
        for word in words:
            t = set(word.lower())  #take set because it doesn't matter how many times the element appears
            if t & a == t:  #word和键盘某一排取交集==word，
                ans.append(word)
            if t & b == t:
                ans.append(word)
            if t & c == t:
                ans.append(word)
        return ans

    def findWords1(self, words):
        ans = []
        hash = {}
        f = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        s = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        t = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        for ele in f:
            hash[ele] = 1
        for ele in f:
            hash[ele] = 2
        for ele in f:
            hash[ele] = 3
        for word in words:
            for char in word:
                num = hash[char]

if __name__ == "__main__":
    nums = ["Hello","Alaska","Dad","Peace"]
    x = Solution()
    print x.findWords(nums)
