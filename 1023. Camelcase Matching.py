class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            res.append(self.camel_match(query, pattern))
        return res

    def camel_match(self, query, pattern):
        i = 0
        j = 0
        while i < len(query) and j < len(pattern):
            # 如果匹配上，一起往下走
            if query[i] == pattern[j]:
                i += 1
                j += 1
            # 如果没匹配上，对应的query是小写，query往下走
            elif query[i].islower():
                i += 1
            # 如果没匹配上，对应的query是大写，invalid
            else:
                return False
        # 如果pattern没用完，invalid
        if j < len(pattern):
            return False
        # 如果 query还剩，里面有大写字母，invalid
        for k in range(i, len(query)):
            if query[k].isupper():
                return False
        return True
