import itertools
class Solution:
    def braceExpansionII(self, expression):
        # expression.strip('"')
        n = len(expression)
        node_stack = []
        start = 0
        node_stack.append(Node())
        for i in range(n):
            if expression[i] == '{':
                if expression[start: i]:
                    node_stack[-1].array.add(expression[start: i])
                new_node = Node()
                start = i + 1
                node_stack.append(new_node)
            elif expression[i].isalpha():
                continue
            elif expression[i] == ',':
                if expression[start: i]:
                    node_stack[-1].array.add(expression[start: i])
                    start = i + 1
            elif expression[i] == '}':
                if expression[start: i]:
                    node_stack[-1].array.add(expression[start: i])
                node = node_stack.pop()
                if len(node_stack[-1].array) == 0:
                    new_array = node.array
                else:
                    new_array = itertools.product(node_stack[-1].array, node.array)
                node_stack[-1].array = set([''.join(ele) for ele in new_array])
                start = i + 1
        return node_stack[0].array


class Node:
    def __init__(self):
        self.string = ''
        self.array = set()

s = Solution()
a = "{a,b}{c{d,e}}"
print(s.braceExpansionII(a))
