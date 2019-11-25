# 对称数
# 题： numbers "69", "88", and "818" are all strobogrammatic.
# 解题：翻转后对称的数就那么几个，我们可以根据这个建立一个映射关系：8->8, 0->0, 1->1, 6->9, 9->6
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hash = {}
        hash['1'] = '1'
        hash['0'] = '0'
        hash['9'] = '6'
        hash['6'] = '9'
        hash['8'] = '8'
        i = 0
        j = len(num) - 1
        while i <= j:
            if num[i] not in hash or hash[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        return True
if __name__ == '__main__':
    a = "egg"
    b = "add"
    s = Solution()
    print(s.isIsomorphic(a,b))

