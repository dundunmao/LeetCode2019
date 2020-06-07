from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        wordset = set(words)
        # 按长度排序，从长到短，如果一样长，按字典序排
        words.sort(key=lambda c: (-len(c), c))
        for word in words:
            # 没拿出一个，只要所有缩短一步的都在set里就找到了
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word
        return ""


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        words.sort(key=lambda x: (-len(x), x))

        for word in words:
            flag = True
            for i in range(1, len(word)):
                if not trie.search(word[:i]):
                    flag = False
                    break
            if flag is True:
                return word
        return ''


class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word):
        cur = self.trie
        for cha in word:
            index = ord(cha) - 97
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.is_word = True

    def search(self, word):
        cur = self.trie
        for cha in word:
            index = ord(cha) - 97
            if not cur.children[index]:
                return False
            cur = cur.children[index]
        return cur.is_word


class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.is_word = False
s = Solution()
a = ["w","wo","wor","worl","world"]
print(s.longestWord(a))
