class Solution:
    def numMatchingSubseq(self, S: str, words) -> int:
        res = 0
        heads = [[] for i in range(26)]
        for word in words:
            heads[ord(word[0]) - 97].append(Node(word, 0))
        for c in S:
            old = heads[ord(c) - 97]
            heads[ord(c) - 97] = []

            for node in old:
                node.index += 1
                if node.index == len(node.word):
                    res += 1
                else:
                    heads[ord(node.word[node.index]) - 97].append(node)
        return res

class Node:
    def __init__(self, word, index):
        self.word = word
        self.index = index

x = Solution()
S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# print(x.numMatchingSubseq(S, words))
# S = "rwpddkvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvjubjgloeofnpjqlkdsqvruvabjrikfwronbrdyyjnakstqjac"
# words = ["wpddkvbnn","lnagtva","kvbnnuglnagtvamxkqtwhqgwbqgfbvgkwyuqkdwhzudsxvju","rwpddkvbnnugln","gloeofnpjqlkdsqvruvabjrikfwronbrdyyj","vbgeinupkvgmgxeaaiuiyojmoqkahwvbpwugdainxciedbdkos","mspuhbykmmumtveoighlcgpcapzczomshiblnvhjzqjlfkpina","rgmliajkiknongrofpugfgajedxicdhxinzjakwnifvxwlokip","fhepktaipapyrbylskxddypwmuuxyoivcewzrdwwlrlhqwzikq","qatithxifaaiwyszlkgoljzkkweqkjjzvymedvclfxwcezqebx"]
# print(x.numMatchingSubseq(S, words))
S = "abacde"
words = ["aace"]
print(x.numMatchingSubseq(S, words))

