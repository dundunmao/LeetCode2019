from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_degree = [0 for i in range(numCourses)]
        if prerequisites == None or len(prerequisites) == 0:
            return True
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
        while len(q) != 0:
            course = q.popleft() #q中取出一门课
            list = hash[course]  #在hash里找到这个课的后续课的list
            for i in range(0,len(list)): #对于list里的所以课，都在in_degree里把他的前置课个数减1，如果减完为0了，就把这课加入q
                in_degree[list[i]] -= 1
                if in_degree[list[i]] == 0:
                    q.append(list[i])
        # 遍历一遍in_degree,看是不是都为0了。
        for i in range(0,numCourses):
            if in_degree[i] != 0:
                return False
        return True

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
                return False

        return len(result) == n

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

if __name__ == "__main__":
    s = Solution()
    a = 7
    b =[[4,1],[4,1],[6,4],[5,2],[5,3],[6,5]]
    print s.canFinish(a,b)
    a =2
    b =[[1,0]]
    print s.canFinish(a,b)
    a =2
    b =[[1,0],[0,1]]
    print s.canFinish(a,b)
