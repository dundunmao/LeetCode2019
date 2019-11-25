# class Solution:
#     def alienOrder(self, words) -> str:
#         string_to_children_hash = {}
#         for word in words:
#             for i in range(len(word)):
#                 if i == len(word) - 1:
#                     string_to_children_hash[word[i]] = []
#                 elif word[i] in string_to_children_hash and word[i + 1] not in string_to_children_hash[word[i]] and word[i + 1] != word[i]:
#                     string_to_children_hash[word[i]].append(word[i + 1])
#                 else:
#                     string_to_children_hash[word[i]] = [word[i + 1]]
#         for i in range(len(words)):
#             if i == len(words) - 1:
#                 string_to_children_hash[words[i][0]] = []
#             elif words[i][0] in string_to_children_hash and words[i + 1][0] not in string_to_children_hash[words[i][0]] and words[i + 1][0] != words[i][0]:
#                 string_to_children_hash[words[i][0]].append(words[i + 1][0])
#             else:
#                 string_to_children_hash[words[i][0]] = [words[i + 1][0]]
#         visited = set()
#         result = []
#         for string, children in string_to_children_hash.items():
#             self.dfs(string, visited, result, children, string_to_children_hash)
#         return ''.join(result)
#
#     def dfs(self, string, visited, result, children, string_to_children_hash):
#         if string in visited:
#             return
#         for child in children:
#             child_children = string_to_children_hash[child]
#             self.dfs(child, visited, result, children, string_to_children_hash)
#         result.append(string)
#         visited.add(string)
#         return


class Solution:
    def alienOrder(self, words) -> str:
        children_hash = {} #每一个char的children
        all_chars = set()
        for word in words:
            for i in range(len(word)):
                all_chars.add(word[i])
        # 拿到每一个char的children的list
        for i in range(1, len(words)):
            cur_word = words[i]
            prev_word = words[i - 1]
            index = 0
            while index < len(cur_word) and index < len(prev_word) and cur_word[index] == prev_word[index]:
                index += 1
            if index < len(cur_word) and index < len(prev_word):
                cur_char = cur_word[index]
                prev_char = prev_word[index]
                if prev_char in children_hash:
                    cur_set = children_hash[prev_char]
                else:
                    cur_set = set()

                cur_set.add(cur_char)
                children_hash[prev_char] = cur_set

        result = []
        # 某node拿到答案是什么（即，是不是走到他并且加进result里了）
        visited_result = [None] * 26
        # 经没经过此node
        pass_by = [False] * 26

        for cur_char in all_chars:
            # 如果有环
            if not self.dfs(cur_char, children_hash, result, visited_result, pass_by):
                return ''
        #因为是孩子先加进来的
        result.reverse()
        return ''.join(result)

    def dfs(self, cur_char, children_hash, result, visited_result, pass_by):
        index = ord(cur_char) - 97
        # 拿到过答案
        if visited_result[index]:
            return True
        # 有环
        if pass_by[index]:
            return False
        pass_by[index] = True

        if cur_char in children_hash:
            for next_char in children_hash[cur_char]:
                # 如果当前点走过，说明有环，return False
                if not self.dfs(next_char, children_hash, result, visited_result, pass_by):
                    return False
        # 进不了if，说明他没孩子,到底了，可以加入result了
        # 走完if，说明从底往上返，返到他了
        visited_result[index] = True
        result.append(cur_char)
        return True




s = Solution()
a = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
print(s.alienOrder(a))
# a = ["za","zb","ca","cb"]
# print(s.alienOrder(a))
