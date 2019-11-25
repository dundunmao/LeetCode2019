# A gene string can be represented by an 8-character long string, with choices from "A", "C", "G", "T".
#
# Suppose we need to investigate about a mutation (mutation from "start" to "end"), where ONE mutation is defined as ONE single character changed in the gene string.
#
# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
#
# Also, there is a given gene "bank", which records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.
#
# Now, given 3 things - start, end, bank, your task is to determine what is the minimum number of mutations needed to mutate from "start" to "end". If there is no such a mutation, return -1.
#
# Note:
#
# Starting point is assumed to be valid, so it might not be included in the bank.
# If multiple mutations are needed, all mutations during in the sequence must be valid.
# You may assume start and end string is not the same.
# Example 1:
#
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
#
# return: 1
# Example 2:
#
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
#
# return: 2
# Example 3:
#
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
#
# return: 3

# 方法：典型BFS

import collections


class Solution(object):
    def minMutation(self, start, end, bank):
        class Solution:
            def minMutation(self, start: str, end: str, bank: List[str]) -> int:
                bank_set = set(bank)
                queue = collections.deque()
                gen_set = set()
                queue.append(start)
                gen_set.add(start)
                level = 0
                while len(queue) > 0:
                    size = len(queue)
                    for i in range(size):
                        cur = queue.popleft()
                        if cur == end:
                            return level
                        lenght = len(cur)
                        for j in range(lenght):
                            for ele in ['A', 'C', 'G', 'T']:
                                temp = cur[:j] + ele + cur[j + 1:]
                                if temp not in gen_set and temp in bank_set:
                                    gen_set.add(temp)
                                    queue.append(temp)
                    level += 1
                return -1


if __name__ == "__main__":
    a = "AACCTTGG"
    b = "AATTCCGG"
    c = ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]

    s = Solution()
    print(s.minMutation(a,b,c))
