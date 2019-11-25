class Solution1:
    def removeComments(self, source):
        res = []
        size = len(source)
        i = 0
        while i < size:
            line = source[i]
            # get block
            if line.strip().startswith("/*"):
                j = i
                while j < size:
                    block_line = source[j]
                    if not block_line.strip().endswith("*/"):
                        j += 1
                    else:
                        break
                i = j + 1
                continue
            if not line.startswith("//"):
                res.append(line)
            i += 1
        return res


class Solution:
    def removeComments(self, source):
        res = []
        block_start = False
        line_comment = False
        block_end = False
        for line in source:
            for i in range(len(line)):
                if i + 2 <= len(line) and line[i: i + 2] == '/*' and not block_start:
                    block_start = True

                if i + 2 <= len(line) and line[i: i + 2] == '*/' and block_start:
                    block_end = True
                    break
                elif i + 2 <= len(line) and line[i: i + 2] == '//' and not block_start:
                    line_comment = True
                    break

            if not block_start and not line_comment:
                res.append(line)
            if block_end == True:
                block_end = False
                block_start = False
            if line_comment:
                line_comment = False


        return res

#####
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        size = len(source)
        i = 0
        block_start = False
        line_comment = False
        for line in source:
            for i in range(len(line)):
                if i + 2 <= size and line[i: i + 2] == '/*' and not block_start:
                    block_start = True
                    break
                elif i + 2 <= size and line[i: i + 2] == '//' and not block_start:
                    line_comment = True
                    break
                elif i + 2 <= size and line[i: i + 2] == '/*' and block_start:
                    block_end = True
                    break

        if not block_start and not line_comment:
            res.append(line)
            line_comment = False
            if block_end == True:
                block_end = False
                block_start = False

        return res
#######
s = Solution()
a = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
print(s.removeComments(a)) # ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
b = ["a/*comment", "line", "more_comment*/b"]
print(s.removeComments(b)) # ["ab"]
