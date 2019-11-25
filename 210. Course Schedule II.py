# 给n门课，一些课是另一些的前置课，
# For example:
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].
# 问上课的顺序
# 这题基本上就是lintcode：/topological-sorting/那道题，一模一样
class Graph_node():
    def __init__(self,x):
        self.v = x
        self.neighbors = []

from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        graph = []
        #创建graph node,放hash的key里
        for i in range(numCourses):
            graph.append(Graph_node(i))
        #把neighbors加进去
        for i in range(numCourses):
            for ele in prerequisites:
                if ele[1] == graph[i].v:
                    graph[i].neighbors.append(graph[ele[0]])
        # 创建in-degree的hash
        hash = {}
        for node in graph:
            hash[node] = 0
        # 把每个node的in-degree算出来
        for node in hash:
            for nerbor in node.neighbors:  #一旦发现某个node是属于edge的，他的in-degree就加一。
                hash[nerbor] += 1

        # BFS
        q = deque()
        #先把in-degree为0的都加入queue里，也放入res里
        for node in hash:
            if hash[node] == 0:
                q.append(node)
                res.append(node.v)
        # 开始pop,每pop一个，就把他的每一个邻居的in-degree -1，如果邻居的in-degree为0了，就让入queue和res里
        while len(q) != 0:
            node = q.popleft()
            for ele in node.neighbors:
                hash[ele] -= 1
                if hash[ele] == 0:
                    res.append(ele.v)
                    q.append(ele)
        # 如果并没有把所以的node都存入res，说明有环，这种情况就return 【】
        if len(res) != numCourses:
            return []
        return res



from collections import deque
class Solution1(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_degree = [0 for i in range(numCourses)]
        hash = {i:[] for i in range(numCourses)}
        # 遍历input，
        # 建 hash：每个课的后续课有哪些
        # 建 in_degree：每个课作为后续课，它的前置课有几个
        # 在prerequisites里，index=0是后续课，index=1是前置课
        for i in range(len(prerequisites)):
            in_degree[prerequisites[i][0]] += 1 #每门课作为后续课出现的次数，也就是每门课在index=0的位置出现一次就记一次
            hash[prerequisites[i][1]].append(prerequisites[i][0]) #每门课作为前置课时，他的后续可往他的value里加，也就是
        q = deque()
        # 先把indegree为0的都加入q里
        for i in range(0,numCourses):
            if in_degree[i] == 0:
                q.append(i)
        #开始进行BFS
        res = []
        while len(q) != 0:
            course = q.popleft() #q中取出一门课
            res.append(course)
            list = hash[course]  #在hash里找到这个课的后续课的list
            for i in range(0,len(list)): #对于list里的所以课，都在in_degree里把他的前置课个数减1，如果减完为0了，就把这课加入q
                in_degree[list[i]] -= 1
                if in_degree[list[i]] == 0:
                    q.append(list[i])
        # 遍历一遍in_degree,看是不是都为0了。
        for i in range(0,numCourses):
            if in_degree[i] != 0:
                return []
        return res


class Solution2(object):
    def findOrder(self, numCourses, prerequisites):
        in_degree = [0 for i in range(numCourses)]  #
        res = [0 for i in range(numCourses)]
        if numCourses <= 0 or prerequisites == None:
            return res
        hash = {i:[] for i in range(numCourses)}
        for pair in prerequisites:
            in_degree[pair[0]] += 1  #建in_degree，是课(index)vs其前置课各数(element)
            hash[pair[1]].append(pair[0])  # 建hash，是课跟其后续课们的关系
        first = 0  #指针
        last = 0
        for i in range(numCourses): #把原始指针一个放在头，一个放在空的位置
            if in_degree[i] == 0:
                res[last] = i
                last += 1
        while first < last:
            if last >= numCourses:
                break
            courses = hash[res[first]]  #每次按照first指的位置，挨个取出其在hash里的list
            if courses != []:
                for item in courses:  #对应list里的每个course,去indegree里找其对应的前置课的个数，减一
                    in_degree[item] -= 1
                    if in_degree[item] == 0:  #一旦为0了，就把他加在last指的位置，last再往后指一个
                        res[last] = item
                        last += 1
                        if last >= numCourses:
                            break
            first += 1
        if last != numCourses:
            return []
        return res


####################
# dfs
class Solution4:
    def findOrder(self, n, prerequisites):

        adjancency_lists = [[] for i in range(n)] # [[], [0], [0], [1, 2]]

        for pre in prerequisites:
            # pre[0] 号 node的 child 里加一个pre[1], 因为pre[0]依赖pre[1]
            # 所以pre[1]是pre[0]的child
            adjancency_lists[pre[0]].append(pre[1])

        result = []
        vistied_result = [False] * n
        vistied_passby = [False] * n
        for i in range(n):
            if not self.dfs(adjancency_lists, i, vistied_result, vistied_passby, result):
                return []
        return result

    # 对于adjancency_lists里的第node_id个node的孩子们（children）,都走一遍，走到底，就是走到叶子节点了，就把他加进res里
    def dfs(self, adjancency_lists, node_id, vistied_result, vistied_passby, result):
        # 已经拿到结果了
        if vistied_result[node_id]:
            return True
        # 已经路过了这个node，用来检查有没有环的
        if vistied_passby[node_id]:
            return False
        vistied_passby[node_id] = True
        # 对于当前这个node，把他的孩子走一遍
        for child_id in adjancency_lists[node_id]:
            if not self.dfs(adjancency_lists, child_id, vistied_result, vistied_passby, result):
                return False
        # 把孩子都走完了，就到他自己了，就把他加结果里
        result.append(node_id)
        vistied_result[node_id] = True

        return True
# bfs
import collections
class Solution5:
    def findOrder(self, n, prerequisites):
        res = [0] * n
        k = 0
        indegree = [0] * n
        q = collections.deque()
        for course in prerequisites:
            indegree[course[0]] += 1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                res[k] = i
                k += 1
        while len(q) > 0:
            cur = q.pop()


if __name__ == "__main__":
    s = Solution4()
    # prerequisites = [[1,2], [3], [4], [4], [5]]
    # numCourses = 4
    # print(s.findOrder(numCourses, prerequisites))
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    numCourses = 4
    print(s.findOrder(numCourses, prerequisites))
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2], [1, 3]]  # 有环
    print(s.findOrder(numCourses, prerequisites))
    numCourses = 3
    prerequisites = []
    print(s.findOrder(numCourses, prerequisites))
