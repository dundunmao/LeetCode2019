

class Solution:
    def canCross(self, stones):
        if stones[0] != 0 or stones[1] != 1:
            return False
        hash = {}
        n = len(stones)
        for ele in stones:
            hash[ele] = []
        hash[0].append(0)
        for i in range(n):
            for last_units in hash[stones[i]]:
                for now_units in [last_units-1, last_units, last_units+1]:
                    nxt = stones[i] + now_units
                    if nxt == stones[-1]:
                        return True
                    if now_units > 0 and nxt in hash and (not hash[nxt] or hash[nxt][-1] > now_units):
                        #2号石头3步跳到i上，我现在想4号石头，我可能要小于3步跳到i上，不然就不对了
                        hash[nxt].append(now_units)
        return len(hash[stones[n-1]]) > 0


class Solution1:
    def canCross(self, stones):
        if stones[0] != 0 or stones[1] != 1:
            return False
        return self.helper(stones, 0, 0)

    def helper(self, a, index, last_units): #TreeNode的表达式
        if index == len(a) - 1:
            return True
#拿到三个分支的结果，取or, 来得到本node的结果
        for units in [last_units - 1, last_units, last_units + 1]:
            if units <= 0:
                continue
            next_index = self.find_index(a, index, units)
            if next_index == -1:
                continue
            if self.helper(a, next_index, units):
                return True
        return False

    def find_index(self, a, index, units):
        for next_index in range(index + 1, min(index + units, len(a) - 1) + 1, 1):
            if a[next_index] ==  a[index] + units:
                return next_index
        return -1  

class Solution2:
    def canCross(self, stones):
        if stones[0] != 0 or stones[1] != 1:
            return False
        record = {}
        return self.helper(stones, 0, 0, record)
    def helper(self, a, index, last_units, record):
        if (index, last_units) in record:
            return record[(index, last_units)]
        if index == len(a) - 1:
            record[(index, last_units)] = True
            return True
        for units in [last_units - 1, last_units, last_units + 1]:
            if units <= 0:
                continue
            next_index = self.find_index(a, index, units)
            if next_index == -1:
                continue
            if self.helper(a, next_index, units, record):
                record[(next_index, last_units)] = True
                return True
        record[(next_index, last_units)] = False
        return False
    def find_index(self, a, index, units):
        for next_index in range(index + 1, min(index + units, len(a) - 1) + 1, 1):
            if a[next_index] ==  a[index] + units:
                return next_index
        return -1
########
class Solution5:
    def canCross(self, stones) -> bool:
        all_result = {}
        index = 0
        in_units = 0
        return self.dfs(stones, index, in_units, all_result)

    def dfs(self, stones, index, in_units, all_result):
        # base case
        if index == len(stones) - 1:
            return True
        # general case
        node = DagNode(index, in_units)
        if node in all_result:
            return all_result[node]
        for out_unit in range(in_units - 1, in_units + 2, 1):
            if out_unit > 0:
                next_index = self.find_next_index(stones, index, out_unit)
                if next_index != -1 and self.dfs(stones, next_index, out_unit, all_result):
                    all_result[node] = True
                    return True
        all_result[node] = False
        return False

    def find_next_index(self, stones, index, out_unit):
        for next_index in range(index + 1, min(index + out_unit, len(stones) - 1) + 1, 1):
            #这里的（index + out_unit）是为了减少遍历次数，因为石头位置比index位置肯定稀疏，所以index+2的位置对应的石头位置，肯定在步数内
            if stones[next_index] == stones[index] + out_unit:
                return next_index
        return -1


class DagNode:
    def __init__(self, index, in_units):
        self.index = index
        self.in_units = in_units

    def __hash__(self):
        return hash((self.index, self.in_units))

    def __eq__(self, other):
        return (self.index, self.in_units) == (other.index, other.in_units)


class Solution5:
    def canCross(self, stones) -> bool:
        all_result = {}
        largeset = stones[-1]
        stones = set(stones)
        return self.dfs(0, 0, all_result, stones, largeset)

    def dfs(self, pos, k, all_result, stones, largeset):
        if pos == largeset:
            return True
        if pos > largeset:
            return False
        if (pos, k) in all_result:
            return all_result[(pos, k)]
        else:
            for i in [k - 1, k, k + 1]:
                if pos + i > largeset:
                    continue
                if i > 0 and pos + i in stones:
                    if self.dfs(pos + i, i, all_result, stones, largeset):
                        all_result[(pos, k)] = True
                        return True
        all_result[(pos, k)] = False
        return False

if __name__ == '__main__':
    s = Solution5()
    stones = [0, 2]
    # stones = [0,1,3,4,5,7,9,10,12]
    # stones = [0,1,3,5,6,8,12,17]
    print(s.canCross(stones))
