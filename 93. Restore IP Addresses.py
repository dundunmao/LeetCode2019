class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if s is None or len(s) > 12:
            return res
        path = []
        self.dfs(s, res, path, 0, 0)
        return res
    def dfs(self, s, res, path, segment, index):
        if segment > 4:
            return
        if segment == 4 and index == len(s):
            res.append('.'.join(path))
        else:
            # 把剩下的这块，按1位，2位，3位分割往下走
            for i in range(1, 4):
                if index + i > len(s):
                    break
                cur_num = s[index : index + i]
                if cur_num.startswith('0') and len(cur_num) > 1 or (i == 3 and int(cur_num)) > 255:
                    continue
                path.append(cur_num)
                self.dfs(s, res, path, segment + 1, index + i)
                path.pop()



class Solution1(object):
    def restoreIpAddresses(self, s):
        res = []
        n = len(s)
        for i in range(1,4):
            if i < n-2:
                for j in range(i+1, i+4):
                    if j < n-1:
                        for k in range(j+1, j+4):
                            if k < n:
                                s1 = s[0:i]
                                s2 = s[i:j]
                                s3 = s[j:k]
                                s4 = s[k:n]
                                if self.valid(s1) and self.valid(s2) and self.valid(s3) and self.valid(s4):
                                    res.append(s1 + "." + s2 + "." + s3 + "." + s4)
        return res
    def valid(self, s):
        if len(s) > 3 or len(s) == 0 or s[0] == '0' and len(s) > 1 or int(s) > 255:
            return False
        return True

if __name__ == "__main__":
    s = "25525511135"
    x = Solution()
    print(x.restoreIpAddresses(s))
