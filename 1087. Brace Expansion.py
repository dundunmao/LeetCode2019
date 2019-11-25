class Solution:
    def expand(self, S: str) -> List[str]:
        res = []
        array = []
        self.dfs(S, 0, array, res)
        return res
    def dfs(self, s, index, array, res):
        if index == len(s):
            if len(array) > 0:
                res.append(''.join(array))
            return
        c = s[index]
        pos = len(array)
# 如果一层有多个的
        if c == '{':
            char_list = []
            end_index = index + 1
            while end_index < len(s) and s[end_index] != '}':
                if s[end_index].isalpha():
                    char_list.append(s[end_index])
                end_index += 1
            char_list.sort()
            for ele in char_list:
                array.append(ele)
                self.dfs(s, end_index + 1, array, res)
                array.pop()
# 如果一层有一个的
        elif c.isalpha():
            array.append(s[index])
            self.dfs(s, index + 1, array, res)
            array.pop()

s = Solution()
a = "{a,b,c}d{e,f}"
print(s.expand(a))
