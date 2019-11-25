class TrieNode:
    def __init__(self):
        self.array = [None for i in range(26)]
        self.is_word = False


class MagicDictionary1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def buildDict(self, dict) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            cur = self.root
            for i in range(len(word)):
                char = word[i]
                if cur.array[ord(char) - 97]:
                    cur = cur.array[ord(char) - 97]
                else:
                    cur.array[ord(char) - 97] = TrieNode()
                    cur = cur.array[ord(char) - 97]
            cur.is_word = True


    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        cur = self.root
        return self.dfs(0, word, cur, 0)

    def dfs(self, cur_id, word, parent_node, count):
        if count > 1:
            return False
        if cur_id == len(word):
            return parent_node.is_word and count == 1

        for i in range(26):
            char = ord(word[cur_id]) - 97
            if parent_node.array[i] is None:
                continue
            if char != i:
                if self.dfs(cur_id + 1, word, parent_node.array[i], count + 1):
                    return True
            else:
                if self.dfs(cur_id + 1, word, parent_node.array[i], count):
                    return True
        return False



# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary1()
dict = ["hello", "leetcode"]
obj.buildDict(dict)
word = "hell"
print(obj.search(word))
word = "hhllo"
print(obj.search(word))
word = "hell"
print(obj.search(word))

dict = ["hello","hallo","leetcode"]
obj.buildDict(dict)
word = "hello"
print(obj.search(word))
word = "hhllo"
print(obj.search(word))
