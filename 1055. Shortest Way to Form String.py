class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        #只为了检查target的char都在不在source里
        array = [False for i in range(26)]
        for i in range(len(source)):
            array[ord(source[i]) - 97] = True
        j = 0
        res = 0
        i = 0
        while i < len(target):
            if not array[ord(target[i]) - 97]:
                return -1
            if j < len(source) and source[j] == target[i]:
                j += 1
                i += 1
            elif j < len(source) and source[j] != target[i]:
                j += 1
            if j == len(source):
                j = 0
                res += 1
        # while出来时，target 走完了，source没走完，最后这段没结算过，要结算一次
        if j != 0:
            res += 1
        return res

s = Solution()
source = "ababcd"
target = "abcb"
print(s.shortestWay(source,target))
source = "abc"
target = "abcbc"
print(s.shortestWay(source,target))
source = "aaaaa"
target = "aaaaaaaaaaaaa"
print(s.shortestWay(source,target))

