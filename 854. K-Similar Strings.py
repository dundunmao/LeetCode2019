# dfs
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        all_res_hash = {}
        return self.dfs(A, B, 0, all_res_hash)

    def dfs(self, a, b, start_index, all_res_hash):
        # 走到头了，返回0
        if start_index == len(b):
            return 0
        # create新node，如果node在hash里，直接返回对应答案
        node = Node(a, start_index)
        if node in all_res_hash:
            return all_res_hash[node]

        result = float('inf')
        # 如果start位置，a和b的char一样，start往后走一位
        if a[start_index] == b[start_index]:
            result = self.dfs(a, b, start_index + 1, all_res_hash)
        else:
            # 如果不一样，a从start位置往后找，找到一样的char,就互换，
            # 可能后面有多个一样的，一个换完，拿到答案，要恢复原样，再去看下一个一样的
            for i in range(start_index + 1, len(a)):
                if a[i] == b[start_index]:
                    a = self.swap(a, start_index, i)
                    # 互换完，result+=1，
                    result = min(result, 1 + self.dfs(a, b, start_index + 1, all_res_hash))
                    a = self.swap(a, start_index, i)
        # for循环后拿到这个node的结果，存hash里，返回这个结果
        all_res_hash[node] = result
        return result

    def swap(self, s, i, j):
        return s[: i] + s[j] + s[i + 1: j] + s[i] + s[j + 1:]


class Node:
    def __init__(self, string, start_index):
        self.string = string
        self.start_index = start_index

    def __hash__(self):
        return hash((self.string, self.start_index))

    def __eq__(self, other):
        return ((self.string, self.start_index) == (other.string, other.start_index))


# bfs
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        all_res_hash = set()
        queue = collections.deque()
        level = 0
        queue.append(A)
        all_res_hash.add(A)

        while len(queue) > 0:
            size = len(queue)
            # 进入里面的一层
            for i in range(size):
                cur = queue.popleft()
                if cur == B:
                    return level
                start_index = 0
                temp = cur
                while temp[start_index] == B[start_index]:
                    start_index += 1
                for j in range(start_index + 1, len(temp)):
                    # 如果遍历到的位置A和B的char一样，说明匹配好的，就不用动
                    if temp[j] == B[j] or temp[j] != B[start_index]:
                        continue
                    # 遍历到的位置跟B的start位置char一样时，开始互换
                    if B[start_index] == temp[j]:
                        temp = self.swap(temp, start_index, j)
                        # 把互换好的放到queue里作为下一层准备着
                        queue.append(temp)
                        # 已经进过queue的不用再进了，进去的时候就是他最佳level
                        all_res_hash.add(temp)
                        # 还原回去为同一层下一个单词做准备
                        temp = self.swap(temp, start_index, j)
            level += 1

        return -1

    def swap(self, s, i, j):
        return s[: i] + s[j] + s[i + 1: j] + s[i] + s[j + 1:]


s = Solution()
a = 'abc'
b = 'bca'
print(s.kSimilarity(a, b))
