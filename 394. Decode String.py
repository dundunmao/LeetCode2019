class Solution:
    def decodeString(self, s: str) -> str:
        start = 0
        # res = ''
        node_stack = []
        # fake base case
        node_stack.append(Node(-1))
        # general case
        for i in range(len(s)):
            # 遇到'['，是开始1，生成node，他前面的数字是node的count，2，加入stack
            if s[i] == '[':
                node = Node(int(s[start:i]))
                node_stack.append(node)
                start = i + 1
            # 遇到'['，是结尾，把node pop出来，把string * count 加到爸爸的string里
            elif s[i] == ']':
                # 把我乘倍加到爸爸
                node = node_stack.pop()
                node_stack[-1].string += node.string * node.count
                start = i + 1
            # 遇到字母，直接加到爸爸的string里
            elif s[i].isalpha():
                node_stack[-1].string += s[i]
                start = i + 1
        return node_stack[-1].string


class Node:
    def __init__(self, count):
        self.string = ''
        self.count = count
s = Solution()
print(s.decodeString("3[a[1[b]]]2[bc]"))
s = Solution()
print(s.decodeString("3[a]2[bc]"))


