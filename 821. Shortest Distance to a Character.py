import collections
from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = []
        # 找到所有c的位置，assign start和end
        start = float('-inf')
        end = float('inf')
        target_index = collections.deque()
        for i in range(len(S)):
            if S[i] == C:
                target_index.append(i)
        if len(target_index) == 0:
            return []
        start = target_index.popleft()
        if len(target_index) > 0:
            end = target_index.popleft()
        # 遍历，看每一个S【i】跟start和end的距离
        for i in range(len(S)):
            if i <= start:
                res.append(start - i)
            elif start < i <= end:
                res.append(min(i - start, end - i))
            else:
                start = end
                if len(target_index):
                    end = target_index.popleft()
                else:
                    end = float('inf')
                res.append(min(i - start, end - i))
        return res


class Solution1:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = []
        # 找到所有c的位置，assign start和end
        start = float('-inf')
        target_index = collections.deque()
        for i in range(len(S)):
            if S[i] == C:
                target_index.append(i)
        if len(target_index) == 0:
            return []
        end = target_index.popleft()
        # 遍历，看每一个S【i】跟start和end的距离
        for i in range(len(S)):
            if i > end:
                start = end
                if len(target_index):
                    end = target_index.popleft()
                else:
                    end = float('inf')
            res.append(min(abs(i - start), abs(end - i)))
        return res

s = Solution1()
a = "loveleetcode"
b = "e"
print(s.shortestToChar(a,b))
