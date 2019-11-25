
# 给出一个字符串s和一个词典，判断字符串s是否可以被空格切分成一个或多个出现在字典中的单词。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出
#
# s = "lintcode"
#
# dict = ["lint","code"]
#
# 返回 true 因为"lintcode"可以被空格切分成"lint code"
class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict


    def wordBreak(self, s, dict):
        # write your code here
        if len(dict) == 0 and len(s) == 0:
            return True
        if s is None or len(s) == 0 or len(dict) == 0:
            return False
        can = [False for i in range(len(s)+1)]
        can[0] = True
        max_len = max(dict)
        for i in range(1,len(s)+1):
            for j in range(1,min(i,max_len)+1):
                if not can[i - j]:
                    continue
                word = s[(i-j):i]
                if word in dict:
                    can[i] = True
                    break
        return can[len(s)]


# time limit exceed

class Solution1:
    # @param s: A string s
    # @param dict: A dictionary of words dict

    def wordBreak(self, s, dict):
        if len(dict) == 0 and len(s) == 0:
            return True
        if s is None or len(s) == 0 or len(dict) == 0  :
            return False
        n = len(s)
        f = [False for i in range(n)]
        for k in range(n):
            word = s[0:k+1]
            if word in dict:
                f[k] = True

        for i in range(1,n):
            for j in range(0,i):
                word = s[j+1:i+1]
                if word in dict and f[j]:
                    f[i] = True
        return f[n-1]

#尽量优化版,仍超时;第一个不超时的办法,是j从后往前遍历
class Solution3:
    # @param s: A string s
    # @param dict: A dictionary of words dict

    def wordBreak(self, s, dict):
        if len(dict) == 0 and len(s) == 0:
            return True
        if s is None or len(s) == 0 or len(dict) == 0:
            return False
        n = len(s)
        max_len = max([len(word) for word in dict])
        f = [False for i in range(n)]
        for k in range(n):
            word = s[0:k + 1]
            if word in dict:
                f[k] = True

        for i in range(1, n):
            for j in range(0, i):
                if f[j]:
                    word = s[j + 1:i + 1]
                    if len(word) <= max_len:
                        if word in dict:
                            f[i] = True
                            break

############
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dictionary_set = set(wordDict)
        res = [False for i in range(len(s))]
        for i in range(len(s)):
            if s[0: i + 1] in dictionary_set:
                res[i] = True
                continue
            for j in range(0, i):
                if res[j] and s[j + 1: i + 1] in dictionary_set:
                    res[i] = True
                    break
                else:
                    res[i] = False
        return res[len(s) - 1]

class Solution3:
    def wordBreak(self, s: str, wordDict) -> bool:
        dictionary_set = set(wordDict)
        result = [None for i in range(len(s))]
        return self.dfs(s, len(s) - 1, dictionary_set, result)

    def dfs(self, s, i, dictionary_set, result):
        if result[i] is not None:
            return result[i]

        if s[0: i + 1] in dictionary_set:
            result[i] = True
            return True

        for p in range(0, i):
            if self.dfs(s, p, dictionary_set, result) and s[p + 1: i + 1] in dictionary_set:
                result[i] = True
                return True
        result[i] = False
        return False



class Solution3:
    def wordBreak(self, s: str, wordDict) -> bool:
        dictionary_set = set(wordDict)
        result = [None for i in range(len(s))]
        return self.dfs(s, 0, dictionary_set, result)

    def dfs(self, s, i, dictionary_set, result):
        if result[i] is not None:
            return result[i]

        if s[i: len(s)] in dictionary_set:
            result[i] = True
            return True

        for p in range(i + 1, len(s)):
            if self.dfs(s, p, dictionary_set, result) and s[i: p] in dictionary_set:
                result[i] = True
                return True

        result[i] = False

        return False



class Solution3:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dictionary_set = set(wordDict)
        res = [False for i in range(n + 1)]
        # base case
        res[n] = True
        # general case
        for i in range(n - 1, -1, -1):
            # a[i~n-1] 刚好在dictionary里
            if s[i : n] in dictionary_set:
                res[i] = True
            # a[i~j-1]在dictionary里面，且a[j~n-1]可以break
            for j in range(i + 1, n):
                if res[j] and s[i : j] in dictionary_set:
                    res[i] = True
        return res[0]
######trie

class Solution:
    def wordBreak(self, s: str, wordDict):
        n = len(s)
        trie_word = Trie()
        for word in wordDict:
            trie_word.insert(word)

        res = [False for i in range(n + 1)]
        # base case
        res[n] = True
        # general case
        for i in range(n - 1, -1, -1):
            # a[i~n-1] 刚好在dictionary里
            if trie_word.search(s[i: n]) == 1:
                res[i] = True
                continue
            # a[i~j-1]在dictionary里面，且a[j~n-1]可以break
            for j in range(i + 1, n):
                if res[j]:
                    result = trie_word.search(s[i: j])
                    if result == False:
                        res[i] = False
                        break
                    elif result == True:
                        res[i] = True
                        break

        return res[0]


# class Trie:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode()
#
#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         cur_root = self.root
#         for char in word:
#             index = ord(char) - 97
#             if cur_root.children[index] == None:
#                 cur_root.children[index] = TrieNode()
#             cur_root = cur_root.children[index]
#         cur_root.is_word = True
#
#     def search(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         cur_root = self.root
#         for char in prefix:
#             index = ord(char) - 97
#             if cur_root.children[index] == None:
#                 return False
#             cur_root = cur_root.children[index]
#         if cur_root.is_word == True:
#             return True
#         return None
#
#
# class TrieNode:
#     def __init__(self):
#         self.children = [None] * 26
#         self.is_word = False

######用trie的最优解
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        trie_word = Trie()
        for word in wordDict:
            trie_word.insert(word)
        res = [False for i in range(len(s))]
        for i in range(len(s)):
            cur_root = trie_word.root
            flag = True
            for j in range(i, -1, -1):
                index = ord(s[j]) - 97
                if cur_root.children[index] is None:
                    flag = False
                    break
                cur_root = cur_root.children[index]
                if cur_root.is_word and res[j-1]:
                    res[i] = True
                    break
            if cur_root.is_word and flag:
                res[i] = True
        return res[len(s) - 1]



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
        reverse_word = list(word)[::-1]
        for char in reverse_word:
            index = ord(char) - 97
            if cur_root.children[index] == None:
                cur_root.children[index] = TrieNode()
            cur_root = cur_root.children[index]
        cur_root.is_word = True


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False




if __name__ == "__main__":
    x = Solution10()
    s = "leetcode"
    dict = ["leet","code"]
    print(x.wordBreak(s, dict)) #T
    s = 'applepenapple'
    dict = ["apple", "pen"]
    print(x.wordBreak(s, dict)) #T
    s = 'catsandog'
    dict = ["cats", "dog", "sand", "and", "cat"]
    print(x.wordBreak(s, dict)) #F

