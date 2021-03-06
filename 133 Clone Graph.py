# 克隆一张无向图，图中的每个节点包含一个 label 和一个列表 neighbors。
#
# 数据中如何表示一个无向图？http://www.lintcode.com/help/graph/
#
# 你的程序需要返回一个经过深度拷贝的新图。这个新图和原图具有同样的结构，并且对新图的任何改动不会对原图造成任何影响。
#
# 您在真实的面试中是否遇到过这个题？ Yes
# 样例
# 比如，序列化图 {0,1,2#1,2#2,2} 共有三个节点, 因此包含两个个分隔符#。
#
# 第一个节点label为0，存在边从节点0链接到节点1和节点2
# 第二个节点label为1，存在边从节点1连接到节点2
# 第三个节点label为2，存在边从节点2连接到节点2(本身),从而形成自环。
# 我们能看到如下的图：
#
#    1
#   / \
#  /   \
# 0 --- 2
#      / \
#      \_/
from collections import deque
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}

    def cloneGraph(self, node):
        # write your code here
        if node is None:
            return node
        # 用BFS来traverse图并得到所以nodes
        nodes = self.getNodes(node)

        # copy nodes, 存hash(key->value = old node->new node)
        hash = self.dict
        for each1 in nodes:
            hash[each1] = UndirectedGraphNode(each1.label)

        # copy neighbors
        for each2 in nodes:
            new_node = hash.get(each2)
            for neighbor in each2.neighbors:
                new_neighbor = hash.get(neighbor)
                new_node.neighbors.append(new_neighbor)
        return hash.get(node)

    # 用BFS来traverse图找到所有点，用hash存起来
    def getNodes(self,node):
        queue = deque()
        set = {}
        queue.append(node)
        set[node] = True
        while len(queue) != 0:
            head = queue.popleft()
            for neighbor in head.neighbors:
                if not set.has_key(neighbor):
                    set[neighbor] = True
                    queue.append(neighbor)
        return set



from Queue import Queue


class Solution1:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.hash = {}

    def cloneGraph(self, node):
        if node is None:
            return None
        nodes = self.get_node(node)
        for ele in nodes:
            self.hash[ele] = UndirectedGraphNode(ele.label)
        for ele in nodes:
            new_node = self.hash[ele]
            for nei in ele.neighbors:
                new_nei = self.hash[nei]
                new_node.neighbors.append(new_nei)
        return self.hash[node]

    def get_node(self, node):
        q = Queue()
        set = {}
        q.put(node)
        while q.qsize()>0:
            cur = q.get()
            if not set.has_key(cur):
                set[cur] = True
            if cur.neighbors != []:
                for ele in cur.neighbors:
                    if ele not in set:
                        q.put(ele)
        return set.keys()
if __name__ == '__main__':
    #        TREE 1
    # Construct the following tree
    #          1
    #        /   \
    #      2     3
    #    /   \
    #  4      5
    #        / \
    #       6   7
    #            \
    #             8
    P1 = UndirectedGraphNode(1)
    # P1.neighbors = [P2,P3]
    P1.neighbors = [UndirectedGraphNode(2), UndirectedGraphNode(3)]
    # P2 =
    # P2.neighbors = [P4]
    # P3 = UndirectedGraphNode(3)

    s = Solution1()
    print s.cloneGraph(P1)
