# 给出两个单词（start和end）和一个字典，找到从start到end的最短转换序列
#
# 比如：
#
# 每次只能改变一个字母。
# 变换过程中的中间单词必须在字典中出现。
#
#  注意事项
#
# 如果没有转换序列则返回0。
# 所有单词具有相同的长度。
# 所有单词都只包含小写字母。
#
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
# 一个最短的变换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog"，
#
# 返回它的长度 5
#


from collections import deque
class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        # write your code here
        if wordList is None or endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 1
        q = deque()
        hash_set = set()
        hash_set.add(beginWord)
        q.append(beginWord)
        length = 1
        dict = {}
        for word in wordList: #这个要转成hash，不然后面遍历的时候会超时
            dict[word] = True
        while q:
            le=len(q)  #每一层的长度
            for i in range(le):  #遍历这一层
                cur = q.popleft() #对于这一层的每一个word
                if cur == endWord: #到终点了就返回length
                    return length
                for j in range(len(cur)):  #把这个word的每一个位置的char都替换26遍，看看在不在wordList里。
                    part1 = cur[:j]
                    part2 = cur[j + 1:]
                    for cha in 'abcdefghijklmnopqrstuvwxyz':
                        new = part1+cha+part2
                        if new in dict and new not in hash_set: #如果在wordList里，并且hash里还没有，就是不在前面那些层里，
                            hash_set.add(new) #加入hash
                            q.append(new) #往q里才，制作下一层的q
            length +=1 #记录的是几层
        return 0

#####################################
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dict_set = set(wordList)
        queue = collections.deque()
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)

        level = 1
        while len(queue) > 0:
            size = len(queue)
            for i in range(0, size):
                word = queue.popleft()
                if word == endWord:
                    return level
                cur = word
                for j in range(len(cur)):
                    part1 = cur[:j]
                    part2 = cur[j + 1:]
                    for cha in 'abcdefghijklmnopqrstuvwxyz':
                        new = part1 + cha + part2
                        if new in dict_set and new not in visited:
                            visited.add(new)
                            queue.append(new)
            level += 1
        return 0


# if __name__ == '__main__':
#     start = 'hit'
#     end = "cog"
#     dict = {"hot", "dot", "dog", "lot", "log"}
#     s = Solution()
#     print s.ladderLength( start, end, dict)
if __name__ == '__main__':
    start = "leet"
    end = "code"
    wordList = ["lest","leet","lose","code","lode","robe","lost"]
    s = Solution()
    print(s.ladderLength( start, end, wordList))
