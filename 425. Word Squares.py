from typing import List

class Solution:
    def __init__(self):
        self.trie = Trie()
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        res = []
        temp = []
        # 建trie
        for word in words:
            self.trie.add(word)
        # 以每个word为开头，做dfs
        for word in words:
            temp.append(word)
            pos = 1 #temp里有几个单词，pos就应该是几
            length = len(word)
            self.search(temp, res, pos, length)
            temp.pop()
        return res

    def dfs(self, temp, res, pos, length):
        if pos == length:
            res.append(temp[:])
            return
        # 找以哪个前缀为开始的word们
        prefix = ''
        for ele in temp:
            prefix += ele[pos]
        cur = self.trie
        candidate_list = cur.search_prefix(prefix)
        # 如果没有这样的word，就失败
        if len(candidate_list) == 0:
            return
        # 如果有，就添加进去，再往下遍历
        for cand in candidate_list:
            temp.append(cand)
            self.dfs(temp, res, pos + 1, length)
            temp.pop()


class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_word = False
        self.prefix_array = []
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self, word):
        cur = self.root
        for cha in word:
            if not cur.children[ord(cha) - 97]:
                cur.children[ord(cha) - 97] = TrieNode()
            cur = cur.children[ord(cha) - 97]
            cur.prefix_array.append(word)
        cur.prefix_array.append(word)
    # return prefix array
    def search_prefix(self, prefix):
        cur = self.root
        for cha in prefix:
            if not cur.children[ord(cha) - 97]:
                return []
            cur = cur.children[ord(cha) - 97]
        return cur.prefix_array



s = Solution()
a = ["area","lead","wall","lady","ball"]
print(s.wordSquares(a))
