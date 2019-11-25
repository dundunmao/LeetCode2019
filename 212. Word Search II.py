# class TrieNode:
#     def __init__(self):
#         self.flag = False
#         self.s = ''
#         self.sons = []
#         for i in range(26):
#             self.sons.append(None)
#
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#     def insert(self, word):
#         # Write your code here
#         cur = self.root
#         for i in range(len(word)):
#             c = ord(word[i]) - ord('a')
#             if cur.sons[c] is None:
#                 cur.sons[c] = TrieNode()
#             cur = cur.sons[c]
#         cur.s = word
#         cur.flag = True
#
#     # @param {string} word
#     # @return {boolean}
#     # Returns if the word is in the trie.
#     def search(self, word):
#         # Write your code here
#         cur = self.root
#         for i in range(len(word)):
#             c = ord(word[i]) - ord('a')
#             if cur.sons[c] is None:
#                 return False
#             cur = cur.sons[c]
#         return cur.flag
#
# class Solution:
#     # @param board, a list of lists of 1 length string
#     # @param words: A list of string
#     # @return: A list of string
#     def wordSearchII(self, board, words):
#         result = []
#         tree = Trie()
#         for word in words:
#             tree.insert(word)
#         res = ''
#         for i in range(len(board)):
#             for j in range(len(board[i])):
#                 self.help(board,i,j,tree.root,result,res)
#         return result
#     def help(self,board,x,y,root,result,res):
#         dx = [1, 0, -1, 0]
#         dy = [0, 1, 0, -1]
#         if root.flag is True:
#             if root.s not in result:
#                 result.append(root.s)
#         if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y]==0 or root is None:
#             return
#         if root.sons[ord(board[x][y]) - ord('a')]:
#             for i in range(4):
#                 cur = board[x][y]
#                 board[x][y] = False
#                 self.help(board, x+dx[i], y+dy[i],root.sons[ord(cur) - ord('a')], result, res)
#                 board[x][y] = cur

################################
# 停在叶子

class Solution:

    def findWords(self, board, words):
        word_trie = Trie()
        for word in words:
            word_trie.insert(word)
        res = set()
        path = []
        n = len(board)
        m = len(board[0])
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(n):
            for j in range(m):
                cur = word_trie.root
                char = board[i][j]
                if cur.children[ord(char) - 97]:
                    self.dfs(cur, i, j, path, res, board, direction, visited)
        return res

    def dfs(self, node, row, col, path, res, board, direction, visited):
        path.append(board[row][col])
        char = board[row][col]
        visited[row][col] = True
        cur = node.children[ord(char) - 97]
        if cur.is_word:
            res.add(''.join(path))

        for i, j in direction:
            if 0 <= row + i < len(board) and 0 <= col + j < len(board[0]) and cur.children[ord(board[row + i][col + j]) - 97] and visited[row][col]:
                self.dfs(cur, row + i, col + j, path, res, board, direction, visited)
        path.pop()
        visited[row][col] = False

#停在None
class Solution3:

    def findWords(self, board, words):
        word_trie = Trie()
        for word in words:
            word_trie.insert(word)
        res = set()
        path = []
        n = len(board)
        m = len(board[0])
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(n):
            for j in range(m):
                cur = word_trie.root
                char = board[i][j]
                self.dfs(cur, i, j, path, res, board, direction, visited)
        return res

    def dfs(self, node, row, col, path, res, board, direction, visited):
        if row in [-1, len(board)] or col in [-1, len(board[0])] or node.children[ord(board[row][col]) - 97] is None or visited[row][col]:
            return
        path.append(board[row][col])
        visited[row][col] = True
        cur = node.children[ord(board[row][col]) - 97]
        if cur.is_word:
            res.add(''.join(path))

        for i, j in direction:
            self.dfs(cur, row + i, col + j, path, res, board, direction, visited)
        path.pop()
        visited[row][col] = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
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






if __name__ == '__main__':
    s = Solution3()
    board = [
        ['d','o','a','f'],
        ['a','g','a','i'],
        ['d','c','a','n']
    ]
    words =["dog", "dad", "dgdg", "can", "again"]
    print(s.findWords(board, words))
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(s.findWords(board, words))
    Output: ["eat", "oath"]
    board = [["a","b"], ["a","b"]]
    words = ["ab"]
    print(s.findWords(board, words))

    board = [["b"], ["a"], ["b"], ["b"], ["a"]]
    words = ["baa", "abba", "baab", "aba"]
    print(s.findWords(board, words))

