class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.array = words
        self.hash = {}   #建一个hash,key为每一个word， value为index的array
        for i in range(len(words)):
            if self.hash.has_key(words[i]):
                self.hash[words[i]].append(i)
            else:
                self.hash[words[i]] = [i]
    def shortest(self, word1, word2):
        list1 = self.hash[word1]   #word1的index的array
        list2 = self.hash[word2]   #word2的index的array
        i = 0
        j = 0
        res = float('inf')
        while i < len(list1) and j < len(list2):   #找最小的距离
            res = min(res,abs(list1[i]-list2[j]))
            if list1[i] > list2[j]:
                j += 1
            else:
                i += 1
        return res


        # Your WordDistance object will be instantiated and called as such:
        # obj = WordDistance(words)
        # param_1 = obj.shortest(word1,word2)
if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    word1 = "coding"
    word2 ="practice"
    obj = WordDistance(words)
    print  obj.shortest(word1,word2)
    word1 = "makes"
    word2 ="coding"
    print  obj.shortest(word1, word2)
