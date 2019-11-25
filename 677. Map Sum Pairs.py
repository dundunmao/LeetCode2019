class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()
        self.string_to_integer_map = {}

    def insert(self, key: str, val: int) -> None:
        if key not in self.string_to_integer_map:
            self.insert_trie(key)
        self.string_to_integer_map[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        cur = self.trie
        for i in range(len(prefix)):
            if cur.array[ord(prefix[i]) - 97]:
                cur = cur.array[ord(prefix[i]) - 97]
            else:
                return res
        visited = set()
        self.dfs(cur, visited)
        for ele in visited:
            res += self.string_to_integer_map[ele]
        return res

    def dfs(self, cur, visited):
        if cur.is_word:
            visited.add(cur.word)
        for i in range(26):
            if cur.array[i]:
                pre = cur
                cur = cur.array[i]
                self.dfs(cur, visited)
                cur = pre

    def insert_trie(self, string):
        cur = self.trie
        for i in range(len(string)):
            if cur.array[ord(string[i]) - 97]:
                cur = cur.array[ord(string[i]) - 97]
            else:
                cur.array[ord(string[i]) - 97] = TrieNode()
                cur = cur.array[ord(string[i]) - 97]
        cur.is_word = True
        cur.word = string


class TrieNode:
    def __init__(self):
        self.array = [None for i in range(26)]
        self.is_word = False
        self.word = ''

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
