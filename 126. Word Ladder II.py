# 给出两个单词（start和end）和一个字典，找出所有从start到end的最短转换序列
#
# 比如：
#
# 每次只能改变一个字母。
# 变换过程中的中间单词必须在字典中出现。
#
#  注意事项
#
# 所有单词具有相同的长度。
# 所有单词都只包含小写字母。
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 给出数据如下：
#
# start = "hit"
#
# end = "cog"
#
# dict = ["hot","dot","dog","lot","log"]
#
# 返回
#
# [
#
#     ["hit","hot","dot","dog","cog"],
#
#     ["hit","hot","lot","log","cog"]
#
#   ]
#

# class Solution1:
#     # @param start, a string
#     # @param end, a string
#     # @param dict, a set of string
#     # @return a list of lists of string
#     def getEntry(self, word, index):
#         return word[:index] + word[index + 1:]
#
#     def buildIndexes(self, length, dict):
#         indexes = []
#         for i in range(length):
#             index = {}
#             for word in dict:
#                 entry = self.getEntry(word, i)
#                 words = index.get(entry, [])
#                 words.append(word)
#                 index[entry] = words
#             indexes.append(index)
#         return indexes
#
#     def BFS(self, start, end):
#         self.distance = {}
#         self.distance[start] = 0
#         queue = [start]
#         while len(queue) != 0:
#             head = queue[0]
#             del queue[0]
#             for word in self.getNextWord(head):
#                 if word not in self.distance:
#                     self.distance[word] = self.distance[head] + 1
#                     queue.append(word)
#
#     def DFS(self, curt, target, path):
#         if curt == target:
#             self.results.append(list(path))
#             return
#
#         for word in self.getNextWord(curt):
#             if self.distance.get(word, -2) + 1 == self.distance[curt]:
#                 path.append(word)
#                 self.DFS(word, target, path)
#                 del path[len(path) - 1]
#
#     def getNextWord(self, word):
#         for i in range(len(word)):
#             entry = self.getEntry(word, i)
#             if entry in self.indexes[i]:
#                 for nextWord in self.indexes[i][entry]:
#                     if nextWord != word:
#                         yield nextWord
#     def __init__(self):
#         self.dict = dict
#         self.indexes = self.buildIndexes(len(start), dict)
#         self.BFS(end, start)
#
#         self.results = []
#     def findLadders(self, start, end, dict):
#         if start is None or end is None or len(start) != len(end):
#             return []
#         if start not in dict or end not in dict:
#             return []
#         if start in self.distance:
#             self.DFS(start, end, [start])
#         return self.results

from collections import deque
class DagNode:
    def __init__(self,id,word,depth):
        self.id = id
        self.word = word
        self.depth = depth
        self.parents = []
        self.children = []
class Solution:
    def findLadders(self, start, end, dict):
        graph = self.build_graph(start, end, dict)
        return self.walk_graph(graph, start, end)
    def build_graph(self, start, end, dict):
        id = 0
        begin_node = DagNode(id, start,0)
        id+=1
        graph = {}
        graph[start] = begin_node
        q = deque()
        q.append(begin_node)
        while len(q) != 0:
            cur = q.popleft()
            if cur.word == end:
                break
        # child
            for i in range(0,len(cur.word)): #把目前遍历的这个word的每一个字母都用26个字母替代一遍
                part1 = cur.word[:i]
                part2 = cur.word[i + 1:]
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = part1+char+part2
                    if next_word in dict:   #如果替换好的在dict里，就开始建graph
                        if not graph.has_key(next_word):  #如果这个word还没连进graph
                            next_node = DagNode(id,next_word,cur.depth+1)  #就生成这个word的DagNode,然后加入q,把其parents和cur的children都填好
                            id += 1
                            q.append(next_node)
                            graph[next_word] = next_node
                            cur.children.append(next_node)
                            next_node.parents.append(cur)
                        elif graph[next_word].depth == cur.depth+1:  #如果这个单词已经遍历过，要看是不是其深度刚好是cur的下一层，例如'fog',为什么是1？？？？
                            next_node = graph[next_word]  #如果是，
                            cur.children.append(next_node) #就把这个点放到当前点的children里，
                            next_node.parents.append(cur)  #并把这个点的parents里加上当前点
        return graph

    def walk_graph(self, graph, start, end):
        if not graph.has_key(end):
            return []
        res = {}
        return self.helper(graph, start, end, res)
    def helper(self, graph, start, end, res):
        cur_node = graph[end]
        if res.has_key(end):
            return res[cur_node]
        ans = []
        if end == start:
            # list = [start]
            ans.append([start])
        for parent in cur_node.parents:
            res_parent = self.helper(graph, start,parent.word,res)
            for list in res_parent:
                temp = list[:]
                temp.append(end)
                ans.append(temp)
        res[cur_node] = ans
        return ans

# dfs会超时
class Solution1:
    def findLadders(self, start, end, dict):
        dict = set(dict)
        map = {}
        self.build_map(dict, start, map)
        cur_list = []
        res = []
        cur_list.append(start)
        hash = set()
        hash.add(start)
        self.dfs(cur_list, hash, res, end, map)
        return res

    def build_map(self,dict,start, map):
        for word in dict:
            map[word] = []
            for nxt in dict:
                if self.diff(word,nxt) == 1:
                    map[word].append(nxt)
        if start not in map:
            map[start] = []
            for nxt in dict:
                if self.diff(start, nxt) == 1:
                    map[start].append(nxt)

    def diff(self, s, t):
        count = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                count += 1
        return count
    def dfs(self, cur_list, hash, res, end, map):
        cur = cur_list[-1] #当前list里最尾端的word,一个新的起点
        if cur == end:  #出口，cur_list最后一位已经是end了。
            if len(res) == 0 or len(res[0]) == len(cur_list):#如果跟res里的一样长，就加进去
                res.append(cur_list[:])
            elif len(cur_list) < len(res[0]): #如果比res里的短，就清空res后加进去
                del res[:]
                res.append(cur_list[:])
        elif len(res) == 0 or len(cur_list) < len(res[0]):  #cur_list的长度没有现在在res里的长度长是，可以继续。如果长了就剪枝
            for string in map[cur]:
                if string not in hash:  #hash是查重的，保证这条route上不能重复出现同一个word
                    cur_list.append(string)
                    hash.add(string)
                    self.dfs(cur_list, hash, res, end, map)
                    hash.remove(string)
                    cur_list.pop()


class Solution2:
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        wordList.add(beginWord) #
        next_word_dict = {}
        self.build_map(wordList, next_word_dict)  #每个hash的key是word，value是array of 变一步并且在dict里的
        # route
        cur_list = []
        cur_list.append(beginWord)
        # 去重的hash
        hash_set = set()
        hash_set.add(beginWord)
        res = []
        self.dfs(cur_list, hash_set, res, endWord, next_word_dict)
        return res

    def build_map(self, wordList, next_word_dict):
        for word in wordList:
            next_word_dict[word] = []
            for i in range(0, len(word)):  # 把目前遍历的这个word的每一个字母都用26个字母替代一遍
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char != word[i]:
                        new_word = word[:i] + char + word[i + 1:]
                        if new_word in wordList:  # 如果替换好的在dict里，就开始建graph
                            next_word_dict[word].append(new_word)

    def dfs(self, cur_list, hash_set, res, endWord, next_word_dict):
        cur = cur_list[-1] #当前list里最尾端的word,一个新的起点
        if cur == endWord:  #出口，cur_list最后一位已经是end了。
            if len(res) == 0 or len(res[0]) == len(cur_list):#如果跟res里的一样长，就加进去
                res.append(cur_list[:])
            elif len(cur_list) < len(res[0]): #如果比res里的短，就清空res后加进去
                del res[:]
                res.append(cur_list[:])
        elif len(res) == 0 or len(cur_list) < len(res[0]):  #cur_list的长度没有现在在res里的长度长时，可以继续。如果长了就剪枝
            for next_word in next_word_dict[cur]:
                if next_word not in hash_set:  #hash是查重的，保证这条route上不能重复出现同一个word
                    cur_list.append(next_word)
                    hash_set.add(next_word)
                    self.dfs(cur_list, hash_set, res, endWord, next_word_dict)
                    hash_set.remove(next_word)
                    cur_list.pop()


import collections
class Solution4(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]] #每层都用一个hash存起来，key是word，value是array of 变一步并在wordList里出现的单词
        while layer:
            newlayer = collections.defaultdict(list)  #newlayer={key:[]}
            for word in layer:  #对于这一层的key，
                if word == endWord: #如果到end了，就存下这个word对应的所有路径
                    res.extend(layer[word][:])
                else:
                    for i in range(len(word)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            next_word = word[:i]+c+word[i+1:]
                            if next_word in wordList: #找到下一个word了
                                # newlayer的key是到目前位置的那个word，就是当前route尾部的word，value的到目前位置的route
                                newlayer[next_word]+=[array+[next_word] for array in layer[word]] #从上一层的route接下去一个
            wordList -= set(newlayer.keys())  #出现在这一层的，就从wordList里删除
            layer = newlayer
        return res


import collections


class Solution5:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordList = set(wordList)
        q = collections.deque()
        cur = Node(beginWord)
        cur.path = [beginWord]
        cur.visited.add(beginWord)
        q.append(cur)
        visited = set()
        # visited.add(beginWord)
        # BFS
        ans = []
        flag = False
        while q and flag == False:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                word = cur.word
                path = cur.path
                visited = cur.visited
                if word == endWord:
                    ans.append(path[:])
                    flag = True
                    continue
                for i in range(len(word)):
                    for j in range(26):
                        new = word[:i] + chr(j + 97) + word[i + 1:]
                        if new in wordList and new not in visited:
                            node = Node(new)
                            v = visited.copy()
                            v.add(new)
                            node.path = path[:] + [new]
                            node.visited = v
                            q.append(node)
                            # visited.add(new)
        return ans

class Node:
    def __init__(self, word):
        self.word = word
        self.path = []
        self.visited = set()


if __name__ == '__main__':
    start = 'hit'
    end = "cog"
    dict = ["hot","dot","dog","lot","log","cog","bit","git"]  #[['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]
    s = Solution5()
    print(s.findLadders(start, end, dict))

    start = "cet"
    # end = "ism"
    # dict = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
    # s = Solution4()
    # print s.findLadders(start, end, dict)
