class Solution:
    def validIPAddress(self, IP: str) -> str:
        if self.is_ipv4(IP):
            return "IPv4"
        if self.is_ipv6(IP):
            return "IPv6"
        return "Neither"

    def is_ipv4(self, IP):
        fields = IP.split('.')
        if len(fields) != 4:
            return False
        for f in fields:
            if len(f) == 0:
                return False
            if not f.isdigit():
                return False
            num = int(f)
            if str(num) != f or num > 255:
                return False
        return True

    def is_ipv6(self, IP):
        count = 0
        fields = IP.split(':')
        if len(fields) != 8:
            return False
        for f in fields:
            if len(f) == 0 or len(f) > 4:
                return False
            f = f.upper()
            for i in range(len(f)):
                if not f[i].isdigit() and not 65 <= ord(f[i]) <= 70:
                    return False
        return True

# s = Solution()
# a = "172.16.254.1"
# print(s.validIPAddress(a))
s = Solution()
a = "2001:0db8:85a3:0:0:8A2E:0370:7334"
print(s.validIPAddress(a))
