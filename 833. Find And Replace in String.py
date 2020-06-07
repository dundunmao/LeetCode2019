class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        match = [-1] * len(S)
        start = 0
        res = []

        for i in range(len(indexes)):
            index = indexes[i]
            size = len(sources[i])
            if S[index: index + size] == sources[i]:
                match[indexes[i]] = i
        print(match)
        start = 0
        while start < len(S):
            if match[start] != -1:
                res.append(targets[match[start]])
                start += len(sources[match[start]])
            else:
                res.append(S[start])
                start += 1
        return ''.join(res)
