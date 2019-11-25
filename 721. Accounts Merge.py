import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        node_to_neighbor = {}
        # build graph
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                cur_email = account[i]
                cur = UGNode(name, cur_email)

                if cur not in node_to_neighbor:
                    node_to_neighbor[cur] = []
                if i == len(account) - 1:
                    continue

                after_email = account[i + 1]
                after = UGNode(name, after_email)
                node_to_neighbor[cur].append(after)

                if after not in node_to_neighbor:
                    node_to_neighbor[after] = []
                node_to_neighbor[after].append(cur)

        result = []

        # walk graph
        visited = set()
        for email, neighbor in node_to_neighbor.items():
            start = email
            if start in visited:
                continue
            group = self.bfs(node_to_neighbor, start, visited)
            res = []
            res.append(start.name)
            res.extend(sorted(group))
            result.append(res)

        return result

    def bfs(self, graph, start, visited):
        emails = set()
        queue = collections.deque()
        queue.append(start)
        while len(queue) > 0:
            cur = queue.popleft()
            if cur in visited:
                continue
            visited.add(cur)
            emails.add(cur.email)
            # children
            if cur in graph:

                neighbors = graph[cur]
            else:
                neighbors = []
            for neighbor in neighbors:
                queue.append(neighbor)
        return emails


class UGNode:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __hash__(self):
        return hash((self.name, self.email))

    def __eq__(self, other):
        return (self.name, self.email) == (other.name, other.email)
