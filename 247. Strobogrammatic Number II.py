import collections
class Solution:
    def findStrobogrammatic(self, n: int):
        res = []
        if n == 1:
            return ['0', '1', '8']
        dict_num = {'1': '1', '6': '9', '8': '8', '9': '6', '0': '0'}
        res_even = collections.deque([''])
        res_odd = collections.deque(['0', '1', '8'])

        for i in range(2, n + 1):
            if i % 2 == 0:
                size = len(res_even)
                for i in range(size):
                    ele = res_even.popleft()
                    for key, val in dict_num.items():
                        res_even.append(key + ele + val)
            else:
                size = len(res_odd)
                for i in range(size):
                    ele = res_odd.popleft()
                    for key, val in dict_num.items():
                        res_odd.append(key + ele + val)
        if n % 2 == 0:
            return [ele for ele in res_even if not ele.startswith('0')]
        else:
            return [ele for ele in res_odd if not ele.startswith('0')]


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = []
        if n == 1:
            return ['0', '1', '8']
        dict_num = {'1': '1', '6': '9', '8': '8', '9': '6', '0': '0'}
        return [ele for ele in self.dfs(n, dict_num) if not ele.startswith('0')]

    def dfs(self, n, dict_num):
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        res = []
        cur = self.dfs(n - 2, dict_num)
        for ele in cur:
            for key, val in dict_num.items():
                res.append(key + ele + val)
        return res


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = []
        path = []
        dict_num = {'1': '1', '6': '9', '8': '8', '9': '6', '0': '0'}
        self.dfs(n, dict_num, path, res)
        return res

    def dfs(self, n, dict_num, path, res):
        if n == 0: # 偶数的出口
            if path and path[-1] == '0':
                return
            cur = []
            for i in range(len(path) - 1, -1, -1):
                cur.append(dict_num[path[i]])
            cur_string = ''.join(cur + path[:])
            res.append(cur_string)
            return
        if n == 1: #奇数的出口
            if path and path[-1] == '0':
                return
            cur = []
            for i in range(len(path) - 1, -1, -1):
                cur.append(dict_num[path[i]])
            for ele in ['0', '1', '8']:
                cur_string = ''.join(cur + list(ele) + path[:])
                res.append(cur_string)
            return
        # 进孩子加不同的边
        for key in dict_num.keys():
            path.append(key) #进孩子加边
            self.dfs(n - 2, dict_num, path, res)
            path.pop() #出孩子删边


s = Solution()
print(s.findStrobogrammatic(2))
print(s.findStrobogrammatic(3))
print(s.findStrobogrammatic(4))
print(s.findStrobogrammatic(5))
print(s.findStrobogrammatic(6))
