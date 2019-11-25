import collections
class StreamChecker:

    def __init__(self, words):
        self.word_trie = Trie()
        for ele in words:
            new_word = ele[::-1]
            self.word_trie.insert(new_word)
        self.string_deque = collections.deque()

    def query(self, letter: str) -> bool:
        self.string_deque.appendleft(letter)
        cur_root = self.word_trie.root
        for i in range(len(self.string_deque)):
            index = ord(self.string_deque[i]) - 97
            # 如果找到end，就是True
            if cur_root.is_word is True:
                return True
            # 如果没路走了，就False
            if cur_root.children[index] is None:
                return False
            cur_root = cur_root.children[index]
        # 整个deque走到底了，最后也要看看是不是end
        return cur_root.is_word == True


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_root = self.root
        for char in word:
            index = ord(char) - 97
            if cur_root.children[index] is None:
                cur_root.children[index] = TrieNode()
            cur_root = cur_root.children[index]
        cur_root.is_word = True



class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

s = StreamChecker(["cd","f","kl"])
print(s.query('a'))
print(s.query('b'))
print(s.query('c'))
print(s.query('d'))
print(s.query('e'))
print(s.query('f'))
print(s.query('g'))
print(s.query('h'))
print(s.query('i'))
print(s.query('j'))
print(s.query('k'))
print(s.query('l'))

