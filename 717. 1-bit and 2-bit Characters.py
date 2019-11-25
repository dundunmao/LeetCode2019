class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if bits[-1] != 0:
            return False

        if len(bits) == 1:
            return True

        if bits[0] == 0:
            pre1 = True
        else:
            pre1 = False

        if len(bits) == 2:
            return pre1

        res = False
        pre2 = True

        for i in range(1, len(bits) - 1):
            if (pre1 and bits[i] == 0) or pre2 and bits[i - 1] == 1:
                res = True
            else:
                res = False
            pre2 = pre1
            pre1 = res
        return res


if __name__ == "__main__":
    s = [1,0,0]
    # s = [1, 1, 1, 0]
    s = [0, 1, 0]
    x = Solution()
    print(x.isOneBitCharacter(s))
