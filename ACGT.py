def four_char_string(s, size):
    hash_char = {'A': '0', 'C': '1', 'G': '2', 'T': '3'}
    hash_num = {'0': 'A', '1': 'A', '2': 'G', '3': 'T'}

    for key, val in hash_char.items():
        s = s.replace(key, val)

    string_trie = Trie()
    for i in range(len(s) - size):
        cur_string = s[i: i + size]
        string_trie.insert(cur_string)
    path = []
    res = []
    dfs(string_trie.root, path, res, hash_num)
    return res


def dfs(cur, path, res, hash_num):

    # base case
    if cur.is_word:
        res.append(''.join(path))
        return

    # general case
    for i in range(4):
        node = cur.children[i]
        if node:
            char = hash_num[str(i)]
            path.append(char)
            dfs(node, path, res, hash_num)
            path.pop()


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.hash_char
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur_root = self.root
        for char in word:
            index = int(char)
            if cur_root.children[index] is None:
                cur_root.children[index] = TrieNode()
            cur_root = cur_root.children[index]
        cur_root.is_word = True

class TrieNode:
    def __init__(self):
        self.children = [None] * 4
        self.is_word = False


s = 'AAAACCCCGGTTAAAAC'
size = 10
print(four_char_string(s, size))
