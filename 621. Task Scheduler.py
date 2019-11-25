from collections import Counter
import heapq
# class Solution1(object):
#     def leastInterval(self, tasks, n):
#         """
#         :type tasks: List[str]
#         :type n: int
#         :rtype: int
#         """
#         map = Counter(tasks)
#         q = []
#         for ele in map:
#             heapq.heappush(q,(-map[ele],ele))  #因为heapq返回最小值，所有这里取负数
#         res = 0
#
#         while len(q) > 0:
#             i = 0
#             temp = []
#             while i <= n:
#                 if len(q) > 0:
#                     if heapq.nsmallest(1,q)[0][0]<-1:
#                         cur = heapq.heappop()
#                         temp.append([cur[0]+1,cur[1]])
#                     else:
#                         heapq.heappop(q)
#                 res += 1
#                 if len(q) == 0 and len(temp) == 0:
#                     break
#                 i += 1
#             for ele in temp:
#                 heapq.heappush(q,ele)
#                     # num,cur = heapq.heappop(q)
#                     # res +=1
#                     # if num > 1:
#                     #     heapq.heappush(q,(num+1,cur))
#         return res
#
# class Solution(object):
#     def leastInterval(self, tasks, n):
#         """
#         :type tasks: List[str]
#         :type n: int
#         :rtype: int
#         """
#         map = Counter(tasks)
#         q = []
#         for ele in map:
#             heapq.heappush(q,-map[ele])  #因为heapq返回最小值，所有这里取负数
#         res = 0
#         while len(q) > 0:
#             i = 0
#             temp = []
#             while i <= n:   #一轮，保证最开始出来的那个task的间隔数是n。
#                 if len(q) > 0:
#                     cur = heapq.heappop(q)
#                     if cur < -1:
#                         temp.append(cur+1)
#                 res += 1 #如果q里有task，就是pop一个出来res+=1，如q里已经空了，res还得继续加1，加的就是idel。
#                 if len(q) == 0 and len(temp) == 0:
#                     break
#                 i += 1
#             for ele in temp:
#                 heapq.heappush(q,ele)
#         return res


# 方法一



# class Solution3:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#
#         task_to_freq_hash = {}
#         res = []
#         # 找到每个字符出现的频率
#         for t in tasks:
#             if t in task_to_freq_hash:
#                 task_to_freq_hash[t] += 1
#             else:
#                 task_to_freq_hash[t] = 1
#         # 放heap里
#         task_heap = []
#         for key, val in task_to_freq_hash.items():
#             heapq.heappush(task_heap, Node(key, val))
#         # 每次从heap里取k个，放res里，取的k个再重新放回heap
#         res = 0
#         while len(task_heap) > 0:
#             temp_array = []
#             for i in range(n + 1):
#                 if len(task_heap) == 0:
#                     if len(temp_array) == 0:
#                         return res
#                     else:
#                         res += 1
#                 else:
#                     cur = heapq.heappop(task_heap)
#                     res += 1
#                     if cur.freq > 1:
#                         cur.freq -= 1
#                         temp_array.append(cur)
#
#             for ele in temp_array:
#                 heapq.heappush(task_heap, ele)
#         return res
#
#
# class Node:
#     def __init__(self, char, freq):
#         self.char = char
#         self.freq = freq
#
#     def __lt__(a, b):
#         if a.freq == b.freq:
#             return a.char < b.char
#         return a.freq > b.freq
#
# # 方法2：
#
# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#
#         task_to_freq_hash = {}
#         res = []
#         # 找到每个字符出现的频率
#         for t in tasks:
#             if t in task_to_freq_hash:
#                 task_to_freq_hash[t] += 1
#             else:
#                 task_to_freq_hash[t] = 1
#         max_number_tasks = []
#         maxi_number = 0
#         for task, freq in task_to_freq_hash.items():
#             if freq > maxi_number:
#                 max_number_tasks = [task]
#                 maxi_number = freq
#             elif freq == maxi_number:
#                 max_number_tasks.append(task)
#
#         need_to_fill = (maxi_number - 1) * (n - len(max_number_tasks) + 1)
#         left_task = len(tasks) - len(max_number_tasks) * maxi_number
#
#         if need_to_fill > left_task:
#             return len(max_number_tasks) * maxi_number + need_to_fill
#         else:
#             return len(max_number_tasks) * maxi_number + left_task
#
# if __name__ == '__main__':
#     a = ["A","A","A","B","B","B"]
#     b = 2
#     s = Solution3()
#     print(s.leastInterval(a,b))
#     a = ["1","1","2","1",'2'] # 1,-,-,1,2,-,1,2
#     b = 2
#     s = Solution3()
#     print(s.leastInterval(a,b))
#     a = ["1","1"]  #1,-,-,1
#     b = 2
#     s = Solution3()
#     print(s.leastInterval(a,b))
#     a = ["1","2","1"]   #1,2,-,1
#     b = 2
#     s = Solution3()
#     print(s.leastInterval(a,b))
#     a = ["1","2","1","2","1","2",'2']   #1,2,-,-,1,2-,-,1,2,-,-,-,2
#     b = 3
#     s = Solution1()
#     print(s.leastInterval(a,b))



# 改题：按原顺序输出


class Solution3(object):
    def leastInterval(self, tasks, n):
        if len(tasks) == 0:
            return 0
        hash = {}
        cur_pos = 0 # 到当前位置所有 idle 的累加
        for i in range(len(tasks)):
            if tasks[i] in hash:   #如果之前出现过，就开始查相同task的距离
                if cur_pos - hash[tasks[i]] < n:  #距离不够用
                    move = n - (cur_pos - hash[tasks[i]])  # move指有多少个idle
                    cur_pos += move + 1
                else:     #距离够用，直接把task算到res里
                    cur_pos += 1
            else:
                cur_pos += 1
            hash[tasks[i]] = cur_pos

        return cur_pos
# length 表示等待要assign task 的位置
def cup_time(s, cool_down):
    task_to_pos_hash = {}
    length = 0
    for i in range(len(s)):
        if s[i] in task_to_pos_hash:
            while length - task_to_pos_hash[s[i]] - 1 < cool_down:
                length += 1
        task_to_pos_hash[s[i]] = length
        length += 1
    return length

a = ["1","1","2","1",'2'] # 1,-,-,1,2,-,1,2 | 8
b = 2
s = Solution3()
print(s.leastInterval(a,b))
a = ["1","1"]  #1,-,-,1 | 4
b = 2
s = Solution3()
print(s.leastInterval(a,b))
a = ["1","2","1"]   #1,2,-,1 | 4
b = 2
s = Solution3()
print(s.leastInterval(a,b))
a = ["1","2","1","2","1","2",'2']   #1,2,-,-,1,2-,-,1,2,-,-,-,2 \14
b = 3
s = Solution3()
print(s.leastInterval(a,b))
