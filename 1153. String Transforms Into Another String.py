import string
import collections
class Solution:
    def canConvert(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        dp = {}
        for i, j in zip(s1, s2):
            if i in dp and dp[i] != j:
                return False
            else:
                dp[i] = j
        return len(set(s2)) < 26 # 如果s2占满了26个字母，就没有free的字母破环了

    def convert_step(self, s1: str, s2: str):
        # graph 里的key是s1的，val是s2的
        graph = {}
        for a, b in zip(s1, s2):
            if a in graph and b != graph[a]:
                return -1
            graph[a] = b
        # 找没用过的char
        free = {c for c in string.ascii_lowercase if c not in graph}
        # Remove self-loops
        for a in list(graph.keys()):
            if graph[a] == a:
                graph.pop(a)
        step = 0
        while graph:
            # Find end of chain，就是在s2里，不在s1里的
            tail = {a for a, b in graph.items() if b not in graph}
            # Find head of chain，就是在s1里，不在s2里的
            heads = set(graph.keys()) - set(graph.values())
            # 有tail说明没有环
            if tail:
                # If chain structure exists, peel its tail
                free |= tail
                for a in tail:
                    graph.pop(a)
                    step += 1
            # 有head说明至少是lollipop
            elif heads:
                # There is one lollipop, we need to find parents of the intersection
                a, seen = list(heads)[0], collections.defaultdict(list)
                while len(seen[a]) < 2:
                    seen[graph[a]].append(a)
                    a = graph[a]
                # seen[G[a]] = [last node in handle, last node in cycle]
                graph.pop(seen[a][1])
                step += 1
                free.add(seen[a][1])
            # 有环的，如果有没用过的char，可以用来破环
            elif free:
                # Use free character to break cycle
                a = list(graph.keys())[0]
                graph[free.pop()] = graph[a]
                graph.pop(a)
                step += 1
            # 有环的，如果没有free的char,不可能破环，return -1
            else:
                # No placeholder to break cycle
                return -1
        return step


        # while graph:
        #     # Find end of chain，就是在s2里，不在s1里的
        #     tail = {a for a, b in graph.items() if b not in graph}
        #     # 有tail说明没有环
        #     while tail:
        #         # If chain structure exists, peel its tail
        #         free |= tail
        #     for a in tail:
        #         while a in graph:
        #             graph.pop(a)
        #             step += 1
        #     # 有head说明至少是lollipop
        #     # Find head of chain，就是在s1里，不在s2里的
        #     heads = set(graph.keys()) - set(graph.values())
        #     while heads:
        #         # There is one lollipop, we need to find parents of the intersection
        #         seen = set()
        #         pre = ''
        #         while a not in seen:
        #             step += 1
        #             free.add(a)
        #             seen.add(a)
        #             a = graph[a]
        #             graph.pop(a)
        #         # seen[G[a]] = [last node in handle, last node in cycle]
        #         # graph.pop(seen[a][1])
        #         # step += 1
        #         # free.add(seen[a][1])
        #     # 有环的，如果有没用过的char，可以用来破环
        #     elif free:
        #         # Use free character to break cycle
        #         a = list(graph.keys())[0]
        #         graph[free.pop()] = graph[a]
        #         graph.pop(a)
        #         step += 1
        #     # 有环的，如果没有free的char,不可能破环，return -1
        #     else:
        #         # No placeholder to break cycle
        #         return -1
        # return step

s = Solution()
# s1 = "abcdefghijklmnopqrstuvwxyz"
# s2 = "bcdefghijklmnopqrstuvwxyza"
# print(s.canConvert(s1,s2))
#
# s1 = 'aa'
# s2 = 'bb'
# print(s.convert_step(s1,s2)) # 1
# s1 = 'aa'
# s2 = 'bc'
# print(s.convert_step(s1,s2)) # -1
# s1 = 'abc'
# s2 = 'bcd'
# print(s.convert_step(s1,s2)) # 3 link
# s1 = 'def'
# s2 = 'fde'
# print(s.convert_step(s1,s2)) # 4 cycle
s1 = 'abcdef'
s2 = 'bcdfde'
print(s.convert_step(s1,s2)) # 6 lollipop

s1 = 'abcefg'
s2 = 'bcdgef'
print(s.convert_step(s1,s2)) # 7 link + cycle
