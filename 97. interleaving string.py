class Solution_rockey:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len2 = len(s2)
        len1 = len(s1)
        if len2 + len1 != len(s3):
            return False
        res = [[None for i in range(len2 + 1)] for j in range(len1 + 1)]
        return self.helper(s1, 0, s2, 0, s3, res)

    def helper(self, s1, i, s2, j, s3, res):
        if res[i][j] is not None:
            return res[i][j]

        if i == len(s1) and j == len(s2):
            res[i][j] = True
        elif i == len(s1):
            res[i][j] = (s2[j] == s3[len(s1) + j] and self.helper(s1, len(s1), s2, j + 1, s3, res))
        elif j == len(s2):
            res[i][j] = (s1[i] == s3[len(s2) + i] and self.helper(s1, i + 1, s2, len(s2), s3, res))
        else:
            res[i][j] = ((s1[i] == s3[i + j] and self.helper(s1, i + 1, s2, j, s3, res))
                         or (s2[j] == s3[i + j] and self.helper(s1, i, s2, j + 1, s3, res))
                         )
        return res[i][j]

# 给出三个字符串:s1、s2、s3，判断s3是否由s1和s2交叉构成。
#
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 比如 s1 = "aabcc" s2 = "dbbca"
#
#     - 当 s3 = "aadbbcbcac"，返回  true.
#
#     - 当 s3 = "aadbbbaccc"， 返回 false.
class Solution1:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        # write your code here
        if s1 is None or s2 is None or s3 is None:
            return False
        if len(s3) != len(s1)+len(s2):
            return False
        len1 = len(s1)
        len2 = len(s2)
        f = [[False for j in range(len2 + 1)] for i in range(len1 + 1)]
        # print f
        f[0][0] = True
        for i in range(1,len1+1):
            if s1[i-1] == s3[i-1]:
                f[i][0] = f[i-1][0]
        for j in range(1,len2+1):
            if s2[j-1] == s3[j-1]:
                f[0][j] = f[0][j-1]
        for i in range(1,len1+1):
            for j in range(1, len2+1):
                if s1[i-1] == s3[i+j-1]:
                    f[i][j] = f[i-1][j]
                    if f[i][j]:
                        continue
                if s2[j-1] == s3[i+j-1]:
                    f[i][j] = f[i][j-1]
                    if f[i][j]:
                        continue
        return f[len1][len2]




if __name__ == "__main__":
    # s1 = "sdfjas;dfjoisdufzjkndfasdkfja;sdfa;dfa;dfaskdjhfasdhjdfakhdgfkajdfasdjfgajksdfgaksdhfasdkbfjkdsfbajksdfhakjsdfbajkdfbakdjsfgaksdhgfjkdsghfkdsfgadsjfgkajsdgfkjasdfh"
    # s2 = "dfnakdjnfjkzghdufguweygfasjkdfgb2gf8asf7tgbgasjkdfgasodf7asdgfajksdfguayfgaogfsdkagfsdhfajksdvfbgkadsghfakdsfgasduyfgajsdkfgajkdghfaksdgfuyadgfasjkdvfjsdkvfakfgauyksgfajkefgjkdasgfdjksfgadjkghfajksdfgaskdjfgasjkdgfuyaegfasdjkfgajkdfygadjskfgjkadfg"
    # s3 = "sdfjas;dfjoisdfnakdjnfjkzghdufguwdufzjkeygfasjkdfgb2gf8asf7ndtgbgasjkdfgasodf7asdfgfajkasdksdfguayfgaogfsdkagfsfjadhfajksdvfbgkadsghfa;sdkdsfgasduyfgajsdkfgafajkdghfaksdgfuyadgfas;dfjkdvfjsdkvfakfgauyksa;dgfajkefgjkdasgfdjksffaskdjhfasdhjdfakhdgadjkghfajgfkajdfksdfgaskdjfgasjkdgfuasdjfgajksdfgaksdhfasdkbfjkdsfbajksdfyaegfasdjkfgajkdfygadjskfgjkadfghakjsdfbajkdfbakdjsfgaksdhgfjkdsghfkdsfgadsjfgkajsdgfkjasdfh"
    s1 = 'a'
    s2 = ''
    s3 = 'a'
    s = Solution()
    print(s.isInterleave(s1, s2, s3))
