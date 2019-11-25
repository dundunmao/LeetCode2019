# Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU, find the exclusive time of these functions.
#
# Each function has a unique id, start from 0 to n-1. A function may be called recursively or by another function.
#
# A log is a string has this format : function_id:start_or_end:timestamp. For example, "0:start:0" means function 0 starts from the very beginning of time 0. "0:end:0" means function 0 ends to the very end of time 0.
#
# Exclusive time of a function is defined as the time spent within this function, the time spent by calling other functions should not be considered as this function's exclusive time. You should return the exclusive time of each function sorted by their function id.
#
# Example 1:
# Input:
# n = 2
# logs =
# ["0:start:0",
#  "1:start:2",
#  "1:end:5",
#  "0:end:6"]
# Output:[3, 4]
# Explanation:
# Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1.
# Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
# Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time.
# So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.
# Note:
# Input logs will be sorted by timestamp, NOT log id.
# Your output should be sorted by function id, which means the 0th element of your output corresponds to the exclusive time of function 0.
# Two functions won't start or end at the same time.
# Functions could be called recursively, and will always end.
# 1 <= n <= 100

# 给一个array表示某个程序开始或结束时间点。求每个程序的总共运行时间，
# class Solution(object):
#     def exclusiveTime(self, n, logs):
#         """
#         :type n: int
#         :type logs: List[str]
#         :rtype: List[int]
#         """
#         logs = [ele.split(':') for ele in logs]
#         stack = []
#         stack.append([logs[0][0],logs[0][1],int(logs[0][2]),0,0])  #stack-ele = [id,stadus,start-time,i,interval]
#
#         res = {}
#         for i in range(n):
#             res[i] = 0
#         i = 1
#         while i < len(logs):  #不能用stack ！= 【】这个条件
#             if stack != [] and stack[-1][0] == logs[i][0] and stack[-1][1] == 'start' and logs[i][1] == 'end':
#                 if i == int(stack[-1][3])+1:
#                     interval = int(logs[i][2]) - int(stack.pop()[2]) + 1#如果是连续的，就时间相减+1
#                     res[int(logs[i][0])] += interval  #res-ele = [id:runtime累加]
#                     if stack != []:
#                         stack[-1][4] += interval
#                 else:  #如果不连续，
#                     cur = stack.pop()
#
#                     res[int(logs[i][0])] += int(logs[i][2])-cur[2]-cur[4]+1
#                     interval = int(logs[i][2]) - cur[2] + 1
#                     if stack != []:
#
#                         stack[-1][4] += interval
#                 i += 1
#             else:
#                 stack.append([logs[i][0],logs[i][1],int(logs[i][2]),i,0]) #stack-ele = [id,stadus,start-time,i,interval]
#                 i += 1
#
#         return [ele[1] for ele in sorted(res.items(),key = lambda x:x[0])]
#
# ##############################
# class Solution1:
#     def exclusiveTime(self, n, logs):
#         log_record = [0] * n
#         log_stack = []
#         # fake 爸爸 node，为了当root给前一个点加others_time时不出错
#         log_stack.append(Node(-1, -1))
#         for log in logs:
#             ele = log.split(':')
#             if ele[1] == 'start':
#                 node = Node(int(ele[0]), int(ele[2]))
#                 log_stack.append(node)
#             elif ele[1] == 'end':
#                 node = log_stack.pop()
#                 log_stack[-1].others_time += int(ele[2]) + 1 - node.start_time
#                 log_record[int(ele[0])] += int(ele[2]) + 1 - node.start_time - node.others_time
#         return log_record
#
#
# class Node:
#     def __init__(self, id, start_time):
#         self.id = id
#         self.start_time = start_time
#         self.others_time = 0


# task: start/end:timestamp
# if ele[1] == 'start':
#     node = node(ele[2], ele[0], 0)
#     stack.append(node)

# elif ele[1] == 'end':
#     cur = stack[-1]
#     total_time = ele[2] - cur.start - cur.exclude
#     hash[ele[0]] += total_time


# node(time, task_id, exclude_time)

class Solution:
    def exclusiveTime(self, n: int, logs):
        hash_task_to_time = {}
        stack = []
        stack.append(Node('-1', 0))
        for ele in logs:
            ele = ele.split(':')
            if ele[1] == 'start':
                node = Node(ele[0], int(ele[2]))
                stack.append(node)
            elif ele[1] == 'end':
                cur = stack.pop()
                total_time = int(ele[2]) - cur.start_time - cur.exclude
                if ele[0] in hash_task_to_time:
                    hash_task_to_time[ele[0]] += total_time
                else:
                    hash_task_to_time[ele[0]] = total_time
                stack[-1].exclude += int(ele[2]) - cur.start_time
        return hash_task_to_time


class Node:
    def __init__(self, task, start_time):
        self.task = task
        self.start_time = start_time
        self.exclude = 0
if __name__ == '__main__':
    s = Solution()
    # n = 2
    # logs = ["0:start:0","1:start:2","1:end:5", "0:end:6"] #Output:[3, 4]
    #
    # print s.exclusiveTime(n,logs)
    #
    # n = 1
    # logs = ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"] #Output:[8]
    # print(s.exclusiveTime(n, logs))
    # n = 1
    # logs = ["0:start:0", "0:end:0"]
    # print s.exclusiveTime(n, logs)

    n = 1
    logs =["0:start:0", "0:start:1", "0:start:2", "0:end:3", "0:end:4", "0:end:5"]
    print(s.exclusiveTime(n, logs))

    n = 3 #[1, 1, 2]
    logs =["0:start:0","0:end:0","1:start:1","1:end:1","2:start:2","2:end:2","2:start:3","2:end:3"]
    print(s.exclusiveTime(n, logs))
