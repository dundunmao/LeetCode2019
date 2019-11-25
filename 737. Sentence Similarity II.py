# bfs
import collections
class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs) -> bool:
        n = len(words1)
        m = len(words2)
        if n != m:
            return False
        adjacency = {}
        for pair in pairs:
            if pair[0] in adjacency:
                adjacency[pair[0]].add(pair[1])
            else:
                adjacency[pair[0]] = set([pair[1]])

            if pair[1] in adjacency:
                adjacency[pair[1]].add(pair[0])
            else:
                adjacency[pair[1]] = set([pair[0]])

        for i in range(n):
            if not self.bfs(words1[i], words2[i], adjacency):
                print(i)
                print(words1[i])
                return False
        return True

    def bfs(self, word1, word2, adjacency):
        visited = set()
        q = collections.deque()
        q.append(word1)
        visited.add(word1)
        while len(q) > 0:
            word = q.popleft()
            if word2 == word:
                return True
            if word in adjacency:
                for w in adjacency[word]:
                    if w not in visited:
                        q.append(w)
                        visited.add(w)
        return False


# dfs
class Solution1:
    def areSentencesSimilarTwo(self, words1, words2, pairs) -> bool:
        n = len(words1)
        m = len(words2)
        if n != m:
            return False
        adjacency = {}
        for pair in pairs:
            if pair[0] in adjacency:
                adjacency[pair[0]].add(pair[1])
            else:
                adjacency[pair[0]] = set([pair[1]])

            if pair[1] in adjacency:
                adjacency[pair[1]].add(pair[0])
            else:
                adjacency[pair[1]] = set([pair[0]])

        for i in range(n):
            visited = set()
            if not self.dfs(words1[i], words2[i], adjacency, visited):
                print(i)
                print(words1[i])
                return False
        return True

    def dfs(self, word1, word2, adjacency, visited):
        if word2 == word1:
            return True

        if word1 not in adjacency:
            return False

        visited.add(word1)

        for word in adjacency[word1]:
            if not word in visited and self.dfs(word, word2, adjacency, visited):
                return True

        return False

s = Solution1()
w1 = ["great","acting","skills"]
w2 = ["fine","drama","talent"]
p = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
print(s.areSentencesSimilarTwo(w1,w2,p))
w1 = ["this","summer","thomas","get","really","very","rich","and","have","any","actually","wonderful","and","good","truck","every","morning","he","drives","an","extraordinary","truck","around","the","nice","city","to","eat","some","extremely","extraordinary","food","as","his","meal","but","he","only","entertain","an","few","well","fruits","as","single","lunch","he","wants","to","eat","single","single","and","really","healthy","life"]
w2 = ["this","summer","thomas","get","very","extremely","rich","and","possess","the","actually","great","and","wonderful","vehicle","every","morning","he","drives","unique","extraordinary","automobile","around","unique","fine","city","to","drink","single","extremely","nice","meal","as","his","super","but","he","only","entertain","a","few","extraordinary","food","as","some","brunch","he","wants","to","take","any","some","and","really","healthy","life"]
p = [["good","nice"],["good","excellent"],["good","well"],["good","great"],["fine","nice"],["fine","excellent"],["fine","well"],["fine","great"],["wonderful","nice"],["wonderful","excellent"],["wonderful","well"],["wonderful","great"],["extraordinary","nice"],["extraordinary","excellent"],["extraordinary","well"],["extraordinary","great"],["one","a"],["one","an"],["one","unique"],["one","any"],["single","a"],["single","an"],["single","unique"],["single","any"],["the","a"],["the","an"],["the","unique"],["the","any"],["some","a"],["some","an"],["some","unique"],["some","any"],["car","vehicle"],["car","automobile"],["car","truck"],["auto","vehicle"],["auto","automobile"],["auto","truck"],["wagon","vehicle"],["wagon","automobile"],["wagon","truck"],["have","take"],["have","drink"],["eat","take"],["eat","drink"],["entertain","take"],["entertain","drink"],["meal","lunch"],["meal","dinner"],["meal","breakfast"],["meal","fruits"],["super","lunch"],["super","dinner"],["super","breakfast"],["super","fruits"],["food","lunch"],["food","dinner"],["food","breakfast"],["food","fruits"],["brunch","lunch"],["brunch","dinner"],["brunch","breakfast"],["brunch","fruits"],["own","have"],["own","possess"],["keep","have"],["keep","possess"],["very","super"],["very","actually"],["really","super"],["really","actually"],["extremely","super"],["extremely","actually"]]
print(s.areSentencesSimilarTwo(w1,w2,p))

