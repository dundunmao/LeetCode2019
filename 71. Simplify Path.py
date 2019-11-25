
class Solution(object):
    def simplifyPath(self, path):
        #把每个有效路径存places里，不存‘ ’和‘.’
        places = [p for p in path.split("/") if p!="." and p!=""]
        stack = []
        for p in places:   #对于存好的每个ele
            if p == "..":   #如果是‘..'就从stack里pop一个ele。如果不是就往stack里压入一个ele
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)  #最后把stack用/join起来


class Solution1:
    def simplifyPath(self, path: str) -> str:
        res = []
        i = 0
        while i < len(path):
            if path[i] == '/':
                j = i + 1
                # i占到一个'/'， j找到下一个'/'
                while j < len(path) and path[j] != '/':
                    j += 1
                # 处理多个'/'
                if j == i + 1:
                    i = j
                # 处理有'/./'的情况
                elif path[i + 1: j] == '.':
                    i = j
                # 处理 '/../'的情况
                elif path[i + 1: j] == '..':
                    if res:
                        res.pop()
                    i = j
                # 其他情况，就是'/字母/'的情况
                else:
                    res.append(path[i + 1: j])
                    i = j
        res = '/'.join(res)
        return '/' + res

#简化代码
class Solution2:
    def simplifyPath(self, path: str) -> str:
        res = []
        i = 0
        while i < len(path):

            if path[i] == '/':
                j = i + 1
                while j < len(path) and path[j] != '/':
                    j += 1

                if path[i + 1: j] == '..':
                    if res:
                        res.pop()
                elif j != i + 1 and path[i + 1: j] != '.':
                    res.append(path[i + 1: j])
                i = j
        res = '/'.join(res)
        return '/' + res

s = Solution2()
a = "/home//" # "/home/foo"
b = "/a/./b/../../c/" # "/c"
c = "/a/../../b/../c//.//"# "/c"
print(s.simplifyPath(a))
print(s.simplifyPath(b))
print(s.simplifyPath(c))


