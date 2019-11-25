class TrieNode:
    def __init__(self):
    # Initialize your data structure here.
        self.childs = {}
        self.isWord = False
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            node = node.childs.get(letter)
            if node is None:
                return False
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            node = node.childs.get(letter)
            if node is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)




class TrieNode:
    def __init__(self):
        self.sons = []
        for i in range(26):
            self.sons.append(None)
        self.flag = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        # Write your code here
        cur = self.root
        for i in range(len(word)):
            c = ord(word[i]) - ord('a')
            if cur.sons[c] is None:
                cur.sons[c] = TrieNode()
            cur = cur.sons[c]
        cur.flag = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        # Write your code here
        cur = self.root
        for i in range(len(word)):
            c = ord(word[i]) - ord('a')
            if cur.sons[c] is None:
                return False
            cur = cur.sons[c]
        return cur.flag


    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        # Write your code here
        cur = self.root
        for i in range(len(prefix)):
            c = ord(prefix[i]) - ord('a')
            if cur.sons[c] is None:
                return False
            cur = cur.sons[c]
        return True
################
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
            if cur_root.children[index] == None:
                cur_root.children[index] = TrieNode()
            cur_root = cur_root.children[index]
        cur_root.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_root = self.root
        for char in word:
            index = ord(char) - 97
            if cur_root.children[index] == None:
                return False
            cur_root = cur_root.children[index]
        return cur_root.is_word == True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_root = self.root
        for char in prefix:
            index = ord(char) - 97
            if cur_root.children[index] == None:
                return False
            cur_root = cur_root.children[index]
        return True


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':

    s = Trie()
    s.insert("lintcode")
    print s.search("code")
    # >> > false
    print s.startsWith("lint")
    # >> > true
    print s.startsWith("linterror")
    # >> > false
    s.insert("linterror")
    print s.search("lintcode")
    # >> > true
    print s.startsWith("linterror")
    # >> > true
