class Solution:
    def serialize(self, s):
        start = 1
        new_hash = {}

        word = ''
        for i in range(1, len(s)):
            if s[i] == ':':
                key = s[start: i]
                new_hash[key] = None
                new_hash = {}
                stack.append(node)
            elif s[i] == ':':
                stack[-1].key = s[start: i]
                start = i + 1
            elif s[i] == '}':
                stack[-1].val = s[start: i]
                node = stack.pop()
                stack[-1].val.append(node)
                start = i + 1




class Node:
    def __init__(self):
        self.key = key
        self.val = val

