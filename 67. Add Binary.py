

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'

class Solution1(object):
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        sb = []
        while i >= 0 or j >= 0:
            sum = carry
            if j >= 0:
                sum += b[j] - '0'
                j -= 1
            if i >= 0:
                sum += a[i] - '0'
                i -= 1
            sb.append(sum % 2)
            carry = sum / 2
        if carry != 0:
            sb.append(carry)
        sb.reverse()
        return ''.join(sb)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        carry = 0
        res = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            res.append(str(carry % 2))
            carry = carry // 2
        if carry == 1:
            res.append('1')
        res.reverse()
        return ''.join(res)

if __name__ == '__main__':
    s = Solution1()
    a = '11'
    b = '1'
    print s.addBinary(a,b)
