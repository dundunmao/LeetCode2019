class Solution(object):
    def isPalindrome(self, x):
        # 1，小于0肯定不是。
        # 2，如果最后一位是0，第一位必须是0才行，这种只有0自己
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        new = 0
        while x > new:
            new = new*10+x%10
            x/= 10
        return x == new or x == new/10
