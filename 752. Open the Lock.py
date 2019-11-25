import collections
class Solution:
    def openLock(self, deadends, target):
        deadends_set = set(deadends)
        queue = collections.deque()
        if '0000' in deadends_set:
            return -1
        queue.append('0000')
        visited = set()
        visited.add('0000')
        level = 0
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur == target:
                    return level
                # 遍历cur的每一个位置，把上一个数和下一个数都放queue里，等到下一层处理
                for j in range(len(cur)):
                    cur_num = int(cur[j])
                    pre = str((cur_num - 1) % 10) # 减一个数
                    nxt = str((cur_num + 1) % 10) # 加一个数
                    prev_string = cur[:j] + pre + cur[j + 1:]
                    next_string = cur[:j] + nxt + cur[j + 1:]
                    if prev_string not in visited and prev_string not in deadends_set:
                        queue.append(prev_string)
                        visited.add(prev_string)
                    if next_string not in visited and next_string not in deadends_set:
                        queue.append(next_string)
                        visited.add(next_string)
            level += 1
        return -1

s = Solution()
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(s.openLock(deadends, target))

deadends = ["8888"]
target = "0009"
print(s.openLock(deadends, target))

deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
print(s.openLock(deadends, target))
