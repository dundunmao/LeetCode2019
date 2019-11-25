class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.cur = self.root
        self.sb = []
        # 把 sentences和times,加入trie里
        for i in range(len(times)):
            self.add(sentences[i], times[i])
    # 建trie
    def add(self, sentence, t):
        # 从头开始
        tmp = self.root
        array = []
        for char in sentence:
            index = ord(char)
            if not tmp.children[index]:
                tmp.children[index] = TrieNode()
            tmp = tmp.children[index]
            array.append(tmp) #把这一路经过的node走加到array里

        # 到句子结束了，在结尾的node上加上string和times的信息
        tmp.string = sentence
        tmp.times += t
        # 把这个最后的node，加入这一路下来所有的node的hotlist里
        for node in array:
            node.update(tmp)

    def input(self, c: str):
        res = []
        if c == '#':
            # 把当前sentence建一次trie
            self.add(''.join(self.sb), 1)
            #重置其他
            self.sb = []
            self.cur = self.root
            return []
        else:
            # 当前cha放入sb里
            self.sb.append(c)
            # 走到当前cha这里
            if self.cur:
                self.cur = self.cur.children[ord(c)]
            # 如果这个cha不在trie里，直接返回【】
            if not self.cur:
                return res
            # 在当前cha的node里，拿出hotlist,返回
            for node in self.cur.hot:
                res.append(node.string)
            return res


class TrieNode:
    def __init__(self):
        self.children = [None] * 128
        self.string = ''
        self.times = 0
        self.hot = []
    # 为了hot list定义排序，先按times排，如果一样，按string排
    def __lt__(a, b):
        if a.times == b.times:
            return a.string < b.string
        return a.times > b.times
    # 把一个node加到当前的hot list里，先加进去，排序，size如果大于3，去掉尾巴的
    def update(self, node):
        if node not in self.hot:
            self.hot.append(node)
        self.hot.sort()
        if len(self.hot) > 3:
            self.hot.pop()

s = AutocompleteSystem(['abc','abd','ab'],[3,2,1])
print(s.input('a')) #['abc', 'abd', 'ab']
print(s.input('a')) #[]
print(s.input('#')) #[]
print(s.input('a')) #['abc', 'abd', 'aa']
