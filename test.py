# def water_flower(a, capacity):
#     res = 0
#     left = capacity
#     for i in range(len(a)):
#         if a[i] > left:
#             res += i * 2
#             left = capacity - a[i]
#             if left < 0:
#                 return -1
#         else:
#             left -= a[i]
#
#     return res + len(a)
#
# def compare_string1(a, b):
#     a_array = a.split(',')
#     b_array = b.split(',')
#     res = []
#     count_b = [] #表示b里每个str的num
#     for i in b_array:
#         count_b.append(count_min_char(i))
#     count_a = [0] * 11 #index表示num，ele表示有几个str是这个num的
#     for j in a_array:
#         count = count_min_char(j)
#         count_a[count] += 1
#         #累加，表示有几个str是最少这个num的。
#     for i in range(1, len(count_a)):
#         count_a[i] = count_a[i] + count_a[i - 1]
#     # num表示b里每个str的num，去a里要找比num小一个的num对应多少个str
#     for num in count_b:
#         res.append(count_a[num - 1])
#     return res
#
# def count_min_char(string):
#     array = [0] * 26
#     for cha in string:
#         array[ord(cha) - 97] += 1
#     for i in range(len(array)):
#         if array[i] > 0:
#             return array[i]
#
#
# # 方法2
# def compare_string2(a, b):
#     a_array = a.split(',')
#     b_array = b.split(',')
#     res = []
#     for i in b_array:
#         count = 0
#         for j in a_array:
#             if count_char(j, min(j)) < count_char(i, min(i)):
#                 count += 1
#         res.append(count)
#     return res
# def count_char(string, char):
#     res = 0
#     for ele in string:
#         if ele == char:
#             res += 1
#     return res
# a = 'abcd,aabc,bd,efcfdcc'
# b = 'aaa,aa,a'
# print(compare_string1(a,b))
#
#
#
# a = [2,4,5,1,2]
# c = 6
# print(water_flower(a, c)) # 17
# a = [2,4,5,1]
# c = 6
# print(water_flower(a, c)) # 8
# a = [2, 4, 5]
# c = 6
# print(water_flower(a, c)) # 7
# a =  [2, 2, 1, 1, 2]
# c = 3
# print(water_flower(a, c)) # 13
#
# import collections
# def continous_k(a, k):
#     mini = min(a[:len(a) - k + 1])
#     mini_index = []
#     for i in range(len(a) - k + 1):
#         if a[i] == mini:
#             mini_index.append(i)
#     res = float('inf')
#     for ele in mini_index:
#         res = min(res, trans_to_num(ele, a, k))
#     res_array = collections.deque()
#     while res > 0:
#         res_array.appendleft(res % 10)
#         res = res // 10
#     return res_array
# def trans_to_num(ele, a, k):
#     array = a[ele: ele + k]
#     res = 0
#     j = 0
#     for i in range(len(array) - 1, -1, -1):
#         res += array[i] * 10 ** j
#         j += 1
#     return res
# def continous_k(a, k):
#     start_index = 0
#     for i in range(len(a) - k + 1):
#         if a[i] > a[start_index]:
#             start_index = i
#     return a[start_index: start_index + k]
# a = [1, 4, 3, 2, 5] #[4, 3, 2]
# k = 3
# print(continous_k(a, k))
# a = [1, 4, 3, 2, 5] #[4, 3, 2]
# k = 4
# print(continous_k(a, k))
# a = [3, 1, 2] #[3,22]
# k = 2
# print(continous_k(a, k))
#
# a = [10, 2, 1] #[10,2]
# k = 2
# print(continous_k(a, k))
#
# def solution(A, B):
#     # write your code in Python 3.6
#     if len(A) == 0 or len(B) == 0:
#         return -1
#     res = []
#     # do not rotate first one
#     # A is original, A[0] is target
#     base_a = helper(A[0], A, B)
#     if base_a != -1:
#         res.append(base_a)
#     # B is original, B[0] is target
#     base_b = helper(B[0], B, A)
#     if base_b != -1:
#         res.append(base_b)
#     # rotate first one, result needs + 1
#     # A is original, B[0] is target
#     base_a_rotate = helper(B[0], A, B)
#     if base_a_rotate != -1:
#         res.append(base_a_rotate + 1)
#         # B is original, A[0] is target
#     base_b_rotate = helper(A[0], B, A)
#     if base_b_rotate != -1:
#         res.append(base_b_rotate + 1)
#
#     if len(res) == 0:
#         return -1
#     return min(res)
#
# def helper(target, original, totated):
#     res = 0
#     for i in range(1, len(original)):
#         if original[i] != target and totated[i] == target:
#             res += 1
#         elif original[i] != target and totated[i] != target:
#             res = -1
#             break
#     return res
# a = [2, 4, 6, 5, 2]
# b = [1, 2, 2, 2, 3]
# class SpreadSheet:
#     def __init__(self, num_row, num_col):
#         self.num_row = num_row
#         self.num_col = num_col
#         self.content = [['' for i in range(self.num_col)] for j in range(self.num_row)]
#         self.record_width = [0 for i in range(self.num_col)]
#
#     def edit_content(self, row, col, content):
#         self.content[row][col] = content
#         self.record_width[col] = max(self.record_width[col], len(content))
#
#     def print_spreadsheet(self):
#         for i in range(self.num_row):
#             print('|'.join(self.content[i]))
#
#     def print_pretty(self):
#
#         for i in range(self.num_row):
#             res = []
#             for j in range(self.num_col):
#                 if len(self.content[i][j]) < self.record_width[j]:
#                     make_up = self.record_width[j] - len(self.content[i][j])
#                     res.append(self.content[i][j] + ' ' * make_up)
#                 else:
#                     res.append(self.content[i][j])
#             print('|'.join(res))
#     # def
# spread_sheet = SpreadSheet(4, 3)
# spread_sheet.edit_content(0,0,'bob')
# spread_sheet.edit_content(0,1,'10')
# spread_sheet.edit_content(0,2,'foo')
# spread_sheet.edit_content(1,0,'alice')
# spread_sheet.edit_content(1,1,'5')
#
# spread_sheet.print_spreadsheet()
# spread_sheet.print_pretty()
# spread_sheet.edit_content(1,0,'x')



# def aaa(a):
#     res = 0
#     for i in range(1, a + 1):
#         if i % 15 == 0:
#             res += i * 10
#         elif i % 5 == 0:
#             res += i * 3
#         elif i % 3 == 0:
#             res += i * 2
#         else:
#             res += i
#     return res
#
# a = 1000
# print(aaa(a))

# def aaaa(a):
#     res = []
#
#     # index = ord('N') + 17
#     # while index > 90:
#     #     index = index - 90
#     # print(chr(index + 65 - 1))
#     for i in range(1, 27):
#         res = []
#         for cha in string:
#             index = ord(cha) + i
#             if index > 90:
#                 while index > 90:
#                     index = index - 90
#                 res.append(chr(index + 65 - 1))
#             else:
#                 res.append((chr(index)))
#         print(i, ''.join(res))
#
#
# string = 'SQZUQ'
# print(aaaa(string))


# def aaa(a):
#     count = 0
#     for i in range(5000, 50000):
#         ord(a[i])
#     return count
# print(aaa('LFIHKRVHRMWRXZGVZURHHSLIGLUDZGVI'))


# A = [(-853388, -797447), (-442839, 721091), (-406140, 987734), (-55842, -980970),(-28064, -960562)
# (240773, -871287)
# (273637, 851940)
# (320461, 997514)
# (495045, -667013)
# (757135, -861866)
# (1148386, -439206)
# (1220903, 239470)

# import collections
# def check_function(sum_up):
#     res = []
#     queue = collections.deque()
#     for i in range(0, sum_up):
#         for j in range(0, sum_up + 1):
#             if i + j == sum_up + 1:
#                 res.append((i, j))
#                 if i + 1 < sum_up and j - 1 < sum_up:
#                     queue.append((i + 1, j - 1))
#                 if i - 1 < sum_up and j + 1 < sum_up:
#                     queue.append((i - 1, j + 1))

#
# def find_arguments(f, z):
#     x = 1
#     y = 2 ** 32 - 1
#     res = []
#     while f(x, 1) <= z:
#         y = bin_search(x, y, f, z)
#         if y != -1:
#             res.append([x, y])
#         else:
#             y = 2 ** 32 - 1
#         x += 1
#     return res
#
# def bin_search(x, last_y, f, z):
#     left, right = 1, last_y - 1
#     while left <= right:
#         mid = (left + right) // 2
#
#         if f(x, mid) == z:
#             return mid
#         elif f(x, mid) < z:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# def f(x,y):
#     return x + y
#
# z = 5
# print(find_arguments(f,z))

# class Product:
#     def __init__(self, k ):
#         self.a = []
#         self.product = 1
#         self.index_zero = -1
#         self.k = k
#     def add(self, x):
#         self.a.append(x)
#         size = len(self.a)
#         if len(self.a) <= self.k:
#             if x == 0:
#                 self.index_zero = size - 1
#                 return 0
#             else:
#                 self.product *= x
#                 if self.index_zero != -1:
#                     return 0
#                 return self.product
#         else:
#             if x == 0:
#                 if self.a[size - k - 1] != 0:
#                     self.product = self.product // self.a[size - k - 1]
#                 self.index_zero = size - 1
#                 return 0
#             else:
#                 self.product = self.product * x // self.a[size - k - 1] if self.a[size - k - 1] != 0 else self.product * x
#                 if size - self.index_zero <= k:
#                     return 0
#                 else:
#                     return self.product




# nums = [1, 3, 3, 6, 5, 7, 0, -3, 6, -3]
# k = 3
# s = Product(k)
#
# # print(s.add(1))
# # print(s.add(3))
# # print(s.add(3))
# # print(s.add(6))
# print(s.add(5))
# print(s.add(7))
# print(s.add(0))
# print(s.add(0))
# print(s.add(6))
# print(s.add(-3))
# print(s.add(-3))
#####frog
# def frog_jump(a, k):
#     f = [False for i in range(len(a))]
#     f[0] = True
#     for i in range(1, len(a)):
#         if a[i] == 0:
#             if f[i - 1] == True:
#                 f[i] = True
#             if i - k >= 0 and f[i - k] == True:
#                 f[i] = True
#     return f[-1]
#
# def frog_jump1(a, k1, k2):
#     visited = [None for i in range(len(a))]
#     return dfs(0, visited, k1, k2, a)
# def dfs(start, visited, k1, k2, a):
#     if start == len(a) - 1:
#         visited[start] = True
#         return True
#     if visited[start] is not None:
#         return
#     else:
#         for i in range(k1, k2 + 1):
#             if start + i < len(a) and a[start + i] == 0:
#                 if dfs(start + i, visited, k1, k2, a):
#                     visited[start] = True
#                     return True
#     visited[start] = False
#     return False
#
# # a = [0,0,1,1,0,0,1,1,0]
# # k = 3
# # print(frog_jump(a,k))
# a1 = [0,1,1,0,0,1,1,1,0]
# k1 = 3
# k2 = 4
# print(frog_jump1(a1,k1, k2))
# box and ball

# class BoxBall:
#     def out_from(self, m, start):
#         return self.helper(0, start, 'down', m)
#     def helper(self, i, j, dir, m):
#         if i == len(m) - 1:
#             return j
#         else:
#             if m[i][j] == '\\':
#                 if dir == 'down':
#                     return self.helper(i, j + 1, 'right', m)
#                 elif dir == 'right':
#                     return self.helper(i + 1, j, 'down', m)
#                 else:
#                     return -1
#             elif m[i][j] == '/':
#                 if dir == 'down':
#                     return self.helper(i, j - 1, 'left', m)
#                 elif dir == 'left':
#                     return self.helper(i + 1, j, 'down', m)
#                 else:
#                     return -1
# s = BoxBall()
# m = [['\\', '\\','\\','/','/'],['\\', '\\','\\','/','/'],['/','/','/','\\','\\'],['\\', '\\','\\','/','/'],['/','/','/','/','/']]
# start = 0
# print(s.out_from(m, start))
# def move_target(a, t):
#     n = len(a)
#     for i in range(n - 1, -1, -1):
#         if a[i] == t:
#             j = i - 1
#             while j >= 0 and a[j] == t:
#                 j -= 1
#             if j < 0:
#                 break
#             a[i], a[j] = a[j], a[i]
#     while i >= 0:
#         a[i] = t
#         i -= 1
#     return a
# a = [1,2,4,2,5,7,3,7,3,5]
# t = 5
# print(move_target(a,t))

# def freq(a):
#     for i in range(len(a)):
#         if a[i] > 0:
#             flag = True
#             while flag:
#                 flag = False
#                 idx = a[i] - 1
#                 if idx != i:
#                     if a[idx] > 0:
#                         # swap
#                         a[i] = a[idx]
#                         a[idx] = -1
#                         flag = True
#                     else:
#                         a[i] = 0
#                         a[idx] -= 1
#                 else:
#                     a[idx] = -1
#     return a
# a = [4,4,5,3,4,5]
# print(freq(a))

# class Calculate:
#     def __init__(self):
#         self.save = ''
#         self.cur = ''
#         self.operator = ''
#         self.pre = ''
#
#     def calculate(self, c):
#         if c == '0' and self.cur == '':
#             self.pre = c
#             print('')
#         elif c.isdigit():
#             self.cur += c
#             self.pre = c
#             print(self.cur)
#         elif c == '+' or c == '-':
#             if self.pre == '+' or self.pre == '-':
#                 self.operator = c
#                 print(self.save)
#             elif self.operator == '':
#                 self.save = self.cur
#                 self.cur = ''
#                 self.operator = c
#                 self.pre = c
#                 print(self.save)
#             else:
#                 self.cur = str(self.oper())
#                 self.operator = c
#                 self.save = self.cur
#                 self.cur = ''
#                 self.pre = c
#                 print(self.save)
#
#     def oper(self):
#         if self.operator == '+':
#             return int(self.save) + int(self.cur)
#         elif self.operator == '-':
#             return int(self.save) - int(self.cur)
#         else:
#             return ''
# s = Calculate()
#
# s.calculate('0')
# s.calculate('1')
# s.calculate('2')
# s.calculate('+')
# s.calculate('3')
# s.calculate('-')
# s.calculate('4')
# s.calculate('+')
# s.calculate('-')
# (s.calculate('2'))
# s.calculate('-')

# def matrix_one(a):
#     left = len(a[0])
#     for i in range(len(a)):
#         for j in range(len(a[0])):
#             if a[i][j] == 1 and j < left:
#                 left = j
#                 break
#     return left
#
# def matrix_one1(a):
#     left = len(a[0])
#     end = len(a[0]) - 1
#     for i in range(len(a)):
#         if a[i][end] == 1:
#             end = bianary_search(a[i], 0, end)
#             continue
#     return end
#
# def bianary_search(array, start, end):
#     while start + 1 < end:
#         mid = start + (end - start) // 2
#         if array[mid] == 1:
#             end = mid
#         elif array[mid] == 0:
#             start = mid
#     if array[start] == 1:
#         return start
#     else:
#         return end
#
# def matrix_one2(a):
#     left = len(a[0]) - 1
#     down = 0
#     while left >= 0 and down < len(a):
#         if a[down][left] == 1:
#             left -= 1
#         else:
#             down += 1
#
#     return left + 1
#
#
# # a = [[0,0,1,1], [0,0,0,1],[0,0,0,0],[0,1,1,1]]
# # print(matrix_one2(a))
#
# a = [[0,0,1,1,1], [0,0,0,1,1],[0,0,0,0,1],[1,1,1,1,1]]
# print(matrix_one2(a))
# import random
# def max_index(a):
#     max_num = float('-inf')
#     count = 0
#     res = 0
#     for i in range(len(a)):
#         if a[i] > max_num:
#             count = 1
#             max_num = a[i]
#             res = i
#
#         elif a[i] == max_num:
#             count += 1
#             rdm = random.randint(1, count)
#             if rdm == count:
#                 res = i
#     return res
# a = [11,30,2,30,30,30,6,2,62,62]
# print(max_index(a))


# def binary_search(a, target):
#     start = 0
#     end = len(a) - 1
#     while start + 1 < end:
#         mid = start + (end - start) // 2
#         if a[mid][0] == target:
#             return mid
#         elif a[mid][0] < target:
#             start = mid
#         else:
#             end = mid
#     return start if a[start][0] == target else end
# def subset_target_k(a, k):
#     a.sort()
#     end = len(a) - 1
#     res = 0
#     for i in range(0, len(a)):
#         if a[i] > k:
#             break
#         if end <= i:
#             res += 1
#         else:
#             while end > i and a[i] + a[end] > k:
#                 end -= 1
#             res += 2 ** (end - i)
#     return res
# 
# a = [7,3,6,4,10]
# k = 10
# 
# print(subset_target_k(a, k)) # 13
# 
# a = [6,3,7,4,10,11]
# k = 10
# print(subset_target_k(a, k)) #13
# 
# a = [1,2,3]
# k = 10
# print(subset_target_k(a, k)) # 7
# a = [4,5,3]
# k = 2
# print(subset_target_k(a, k)) # 0
# #duplicate
# 
# a = [1,1,1]
# k = 10
# print(subset_target_k(a, k)) # 7

# class Multi():
#     def multi_prime(self,nums):
#         res = []
#         if len(nums) == 0:
#             return res
#         product = 1
#         pos = 0
#         # nums.sort()
#         self.helper(res, nums, pos, product)
#         return res
#     def helper(self, res, nums, pos, product):
#         if product != 1:
#             res.append(product)
#         for i in range(pos, len(nums)):
#             # if i != pos and nums[i] == nums[i-1]:
#             #     continue
#             product *= nums[i]
#             self.helper(res, nums, i+1, product)
#             product //= nums[i]

# class Multi1:
#     def multi_prime(self, a):
#         res = []
#         product = 1
#         a.sort()
#         self.dfs(a, 0, res, product)
#         return res
#
#     def dfs(self, a, start, res, product):
#         if product != 1:
#             res.append(product)
#         for i in range(start, len(a)):
#             # if i > start and a[i] == a[i - 1]:
#             #     continue
#             product *= a[i]
#             self.dfs(a, i + 1, res, product)
#             product //= a[i]
#
# s = Multi1()
#
# a = [2,2,2]
# print(s.multi_prime(a))
# a = [2,3,5]
# print(s.multi_prime(a))

# def operator(s, target):
#     temp = []
#     res = []
#     # array = [ele for ele in s]
#     dfs(s, 0, 0, target, temp, res)
#     return res
# def dfs(array, start, cur_sum, target, temp, res):
#     if start == len(array):
#         if cur_sum == target:
#             res.append(''.join(temp))
#     else:
#         for i in range(start, len(array)):
#             head = int(array[start: i + 1])
#             if start == 0:
#                 temp.append(str(head))
#                 dfs(array, i + 1, cur_sum + head, target, temp, res)
#                 temp.pop()
#             # "+"
#             temp.append('+' + str(head))
#             dfs(array, i + 1, cur_sum + head, target, temp, res)
#             temp.pop()
#             # "-"
#             temp.append('-' + str(head))
#             dfs(array, i + 1, cur_sum - head, target, temp, res)
#             temp.pop()
# print(operator('123456789', 252))
#
#
#
#
# class Pocker:
#     def __init__(self, p1, p2):
#         self.p1 = {}
#         self.rule = {'2':2,'J': 11, 'Q':12}
#         for ele in p1:
#             cur = self.rule[ele]
#             if ele in p1:
#                 self.p1[cur] += 1
#             else:
#                 self.p1[cur] = 1
#         # 2:3,K:2
#         self.p2 = {}
#     def winner(self):
#         # p1
#         if self.straigt():
#             return p1
#         # p2
#         self.straigt()
#         # p1
#
#         # maxi
#         maxi_p1 = self.high(self, 'p1')
#         maxi_p2 = self.high(self, 'p2')
#         self.run('maxi', 'p1')
#         self.run('maxi', 'p2')
#         if maxi_p1 > maxi_p2:
#             self.run('maxi', 'p1')
#             return 'p1'
#         else:
#             self.run('maxi', 'p2')
#             return 'p2'
#
#
#     def straigt(self, p):
#         # return T or F
#
#     def three_kind
#
#
#     def high(self, player):
#         maxi = 0
#         if player == 'p1':
#             p = self.p1
#         else:
#             p = self.p2
#         for ele in p:
#             if ele > maxi:
#                 maxi = ele
#         return maxi


# def CheckForSequence(arr, n, k):
#     # Traverse the array from end
#     # to start
#     for i in range(n - 1, -1, -1):
#         # if k is greater than
#         # arr[i] then substract
#         # it from k
#         if (k >= arr[i]):
#             k -= arr[i]
#
#             # If there is any subsequence
#     # whose sum is equal to k
#     if (k != 0):
#         return False
#     else:
#         return True
#
#     # Driver code
#
#
# if __name__ == "__main__":
#
#     A = [1, 3, 7, 15, 31]
#     n = len(A)
#
#     if (CheckForSequence(A, n, 18)):
#         print(True)
#     else:
#         print(False)
#
# LinkedIn OA
# import collections
# def find_max_in_min(a, k):
#     start = 0
#     deque = collections.deque()
#     res = float('-inf')
#     for i in range(len(a)):
#         cur = a[i]
#         while len(deque) > 0 and a[deque[-1]] >= cur:
#             deque.pop()
#         deque.append(i)
#
#         if i - start + 1 > k:
#             if start == deque[0]:
#                 deque.popleft()
#             start += 1
#         if i - start + 1 == k:
#             res = max(res, a[deque[0]])
#     return res
# # a = [8,2,4]
# # k = 2
# # print(find_max_in_min(a, k))
# a = [1,3,-1,-3,5,3,6,7,3]
# k = 3
# print(find_max_in_min(a, k))
#
# a = [1,2,3,4,5,4,3,2]
# k = 3
# print(find_max_in_min(a, k))
#
# a = [0,0,0]
# k = 2
# print(find_max_in_min(a, k))

# def arbitrary_shopping(a, tgt):
#     start = 0
#     i = start
#     sum_up = 0
#     res = float('-inf')
#     while i < len(a):
#         while i < len(a) and sum_up + a[i] <= tgt:
#             sum_up += a[i]
#             i += 1
#         if sum_up == tgt:
#             res = max(res, i - start)
#
#         sum_up -= a[start]
#         start += 1
#     return res
# a = [2,3,5,1,1,2,1] # 4
# tgt = 5
# print(arbitrary_shopping(a, tgt))
#
# a = [1,1,1,3,2,1,2,1,1] # 4
# tgt = 5
# print(arbitrary_shopping(a, tgt))


# def threshold_alert(n, numCall, alertThreshold, preceding):
#     start = 0
#     sum_up = 0
#     n = len(numCall)
#     res = 0
#     for i in range(n):
#         sum_up += numCall[i]
#         if i - start + 1 == preceding:
#             if sum_up // preceding > alertThreshold:
#                 res += 1
#             sum_up -= numCall[start]
#             start += 1
#     return res
#
# n = 8
# numCall = [2, 2, 2, 2, 5, 5, 5, 8]
# alertThreshold = 4
# preceding = 3
# print(threshold_alert(n, numCall, alertThreshold, preceding))


# def break_panlim(a):
#     i = 0
#     j = len(a) - 1
#     while i <= j and a[i] == 'a':
#         i += 1
#         j -= 1
#
#     if i >= j:
#         return False
#     else:
#         return a[:i] + 'a' + a[i + 1:]
#
# a = 'a'
# print(break_panlim(a)) #F
# a = 'aba'
# print(break_panlim(a)) #F
# a = 'aaa'
# print(break_panlim(a)) # F
# a = 'abcba'
# print(break_panlim(a)) # 'aacba'




# def double(a, b):
#     # a = set(a)
#     # while b in set(a):
#     #     b *= 2
#     for i in range(len(a)):
#         if a[i] == b:
#             b *= 2
#     return b
# b = 2
# a = [1, 2, 4, 11, 12]
# print(double(a, b))


# def map(a):
#     directions = [(-1,0), (0, 1),(1, 0),(0, -1)] #up，right，down，left
#     row = 0
#     col = 0
#     dir = 0
#     for i in range(4):
#         for ele in a:
#             if ele == 'G':
#                 row += directions[dir][0]
#                 col += directions[dir][1]
#             if ele == 'R':
#                 dir = (dir + 1) % 4
#             if ele == 'L':
#                 dir = (4 + dir - 1) % 4
#     return row == 0 and col == 0 and dir == 0
#
# a = 'G'
# print(map(a))
# a = 'L'
# print(map(a))
# a = 'RG'
# print(map(a))
# a = 'GLLG'
# print(map(a))
# a = 'GL'
# print(map(a))
# a = 'GLG'
# print(map(a))
# a = 'GLGLRG'
# print(map(a))
# a = 'GLRG'
# print(map(a))
# a = 'RGRGLGL'
# print(map(a))
#
#
#
#
#
# comicBook
# coin
# coinsNeeded
# consOfferd
# def xxx(comicBook,coins, coinsNeeded, consOfferd ):
#     res = 0
#     for left in range(comicBook + 1):
#         if left * coinsNeeded <= (comicBook - left) * consOfferd + coins:
#             res = max(res, left)
#     return res
#
# comicBook = 3
# coins = 6
# coinsNeeded = 4
# consOfferd = 5
# print(xxx(comicBook,coins, coinsNeeded, consOfferd))
# comicBook = 10
# coins = 10
# coinsNeeded = 1
# consOfferd = 1
# print(xxx(comicBook,coins, coinsNeeded, consOfferd))
# comicBook = 393
# coins = 896
# coinsNeeded = 787
# consOfferd = 920
# print(xxx(comicBook,coins, coinsNeeded, consOfferd))
# comicBook = 4
# coins = 8
# coinsNeeded = 4
# consOfferd = 3
# print(xxx(comicBook,coins, coinsNeeded, consOfferd))

# import random
#
#
# def selectKItems(stream, n, k):
#     array = [0] * k
#     # 先把前k个存array里
#     for i in range(k):
#         array[i] = stream[i]
#     i = k
#     while (i < n):
#         # 从0到i随机取个数
#         j = random.randrange(i + 1)
#         # j 如果落在k里，求去替换 j 位置的数
#         if (j < k):
#             array[j] = stream[i]
#         i += 1
#     return array

# def getMinimumUniqueSum(arr):
#     # Write your code here
#     if arr is None or len(arr) == 0:
#         return 0
#
#     num_to_freq = [0 for i in range(11)]
#     for i in range(len(arr)):
#         num = arr[i]
#         num_to_freq[num] += 1
#     temp = 0
#     not_fill = 0
#     for i in range(1, 11):
#         if temp == 0 and num_to_freq[i] == 0:
#             not_fill += i
#         elif num_to_freq[i] == 0:
#             temp -= 1
#         elif num_to_freq[i] > 1:
#             temp += 1
#         elif num_to_freq[i] == 1:
#             continue
#     print(not_fill)
#     return (1 + 10) * 10 // 2 - not_fill
# a = [2,2,2,2,2]
# print(getMinimumUniqueSum(a))

# def shuidi(s):
#     i = 0
#     res = ''
#     while i < len(s):
#         count = 1
#         while i < len(s) - 1 and s[i + 1] == s[i]:
#             count += 1
#             i += 1
#         if ord(s[i]) - ord('a') + 1 > 9:
#             res += (str(ord(s[i]) - ord('a') + 1)) + '#'
#         else:
#             res += (str(ord(s[i]) - ord('a') + 1))
#         if count > 1:
#             res += '(' + str(count) + ')'
#         i += 1
#     return res
#
# print(shuidi('back'))#21311#
# print(shuidi('fooood'))
# print(shuidi('aaabbbbaaaa'))
# print(shuidi('sheathery'))

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# class Solution:
#     def __init__(self):
#         self.error = ''
#
#     def ddd(self, a):
#         aj = {}
#         for ele in a:
#             if ele[0] not in aj:
#                 aj[ele[0]] = [ele[1]]
#             else:
#                 aj[ele[0]].append(ele[1])
#         visited = set()
#         head_set = {}
#         for key, child in aj.items():
#             if len(child) > 2:
#                 return 'E1'
#             if key not in visited:
#                 pass_by = set()
#                 node = TreeNode(key)
#                 if not self.dfs(key, visited, aj, pass_by, node, head_set):
#                     return self.error
#                 head_set[key] = node
#         if len(head_set) > 1:
#             return 'E5'
#         else:
#             head = [ele for ele in head_set.values()][0]
#             stack = []
#             stack.append(head)
#             res = []
#             return self.dfs_tree(head)
#     def dfs_tree(self, root):
#         if not root:
#             return ''
#         else:
#             left = self.dfs_tree(root.left)
#             right = self.dfs_tree(root.right)
#             return '(' + str(root.val) + left + right + ')'
#
#
#     def dfs(self, cur, visited, aj, pass_by, node, head_set):
#         if node.val in pass_by: # E3
#             self.error = 'E3'
#             return False
#         elif node.val in head_set:
#             head_set.remove(node.val)
#             return True
#         pass_by.add(node.val)
#         if node.val in aj:
#
#             for child in aj[node.val]:
#                 if child in head_set:
#                     new = head_set[child]
#                 elif child in visited:
#                     self.error = 'E2'
#                     return False
#                 else:
#                     new = TreeNode(child)
#                 if not node.left:
#                     node.left = new
#                 elif not node.right:
#                     node.right = new
#                 else:
#                     self.error = 'E1'
#                     return False
#                 if not self.dfs(child, visited, aj, pass_by, new, head_set):
#                     return False
#         visited.add(node.val)
#         return True
#
# s = Solution()
# a = [('A','C'), ('B','G'), ('C', 'H'), ('B', 'D'), ('C', 'E'), ('A', 'B'), ('E', 'F')]
# print(s.ddd(a))

# def frequency1(s):
#     i = len(s) - 1
#     end = i
#     res = ''
#     count = 1
#     while i >= 0:
#         if s[i] == ')':
#             while s[i] != '(':
#                 i -= 1
#             count = int(s[i + 1: end])
#
#             i -= 1
#             end = i
#         else:
#             count = 1
#         if s[i] == '#':
#             i -= 2
#             ele = s[i:end]
#         else:
#             ele = s[i:end + 1]
#         letter = chr(int(ele) + 97 - 1)
#         for k in range(count):
#             res = letter + res
#         i -= 1
#         end = i
#     tem = [0] * 26
#     for ele in res:
#         index = ord(ele) - 97
#         tem[index] += 1
#     return ''.join([str(ele) for ele in tem])
#
#
#
# def frequency(s):
#     i = len(s) - 1
#     end = i
#     count = 1
#     tem = [0] * 26
#     while i >= 0:
#         if s[i] == ')':
#             while s[i] != '(':
#                 i -= 1
#             count = int(s[i + 1: end])
#             i -= 1
#             end = i
#         else:
#             count = 1
#         if s[i] == '#':
#             i -= 2
#             ele = s[i:end]
#         else:
#             ele = s[i:end+1]
#         index = int(ele) - 1
#         tem[index] += count
#
#         i -= 1
#         end = i
#     return tem
#
#
# print(frequency('25#16#16#18#93(5465)'))
# print(frequency('615#(4)4'))
# print(frequency('1(3)2(4)1(4)'))
# print(frequency('19#85120#8518#25#'))
# import collections
# def possible_word(s):
#     q = collections.deque()
#     hash = set()
#     q.append((s, 0))
#     hash.add((s, 0))
#     res = []
#     while q:
#         cur, start = q.popleft()
#         if start == len(cur):
#             res.append(cur)
#             continue
#         i = start
#         j = i + 1
#         count = 1
#         break_flag = False
#         while j < len(cur):
#             while j < len(cur) and cur[j] == cur[i]:
#                 count += 1
#                 j += 1
#             if count > 2:
#                 new1 = cur[:i] + cur[i] + cur[j:]
#                 q.append((new1, i + 1))
#                 new2 = cur[:i] + cur[i] + cur[i] + cur[j:]
#                 q.append((new2, i + 2))
#                 break_flag = True
#                 break
#             else:
#                 i += 1
#                 j = i + 1
#         if not break_flag:
#             res.append(cur)
#     return res
#
# s = 'leetcooodeee'
# print(possible_word1(s))
#
# s = 'letcooooodee'
# print(possible_word1(s))

s = 'abcdefs'
for i in range(len(s)-1, -1, -2):
    print(s[i])



