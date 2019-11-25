class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        build_trie = Trie()
        for word in dict:
            build_trie.insert(word)
        word_array = sentence.split(' ')
        for i in range(len(word_array)):
            prefix = build_trie.is_prefix(word_array[i])
            if len(prefix) > 0:
                word_array[i] = prefix
        return ' '.join(word_array)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            index = ord(char) - 97
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            if cur.is_word:
                return
        cur.is_word = True
        return

    def is_prefix(self, word):
        cur = self.root
        res = []
        for char in word:
            index = ord(char) - 97
            # 如果发现走不下去，就invalid
            if cur.children[index] is None:
                return ''
            cur = cur.children[index]
            res.append(char)
            # 如果找到is_word,就找到了
            if cur.is_word:
                return ''.join(res)
        return ''


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False
