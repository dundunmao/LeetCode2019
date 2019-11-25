from sortedcontainers import SortedList
import heapq
import django
import json
# class Solution:
#     def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
#         letter_to_freq_license = [0] * 26
#         for ele in licensePlate:
#             if ele.isalpha():
#                 ele = ele.lower()
#                 letter_to_freq_license[ord(ele) - 97] += 1
#
#         size = float('inf')
#         res = None
#         for word in words:
#             if res and len(word) >= len(res):
#                 continue
#             letter_freq_word = [0] * 26
#             stop = False
#             for ele in word:
#                 letter_freq_word[ord(ele) - 97] += 1
#             for i in range(26):
#                 if letter_to_freq_license and letter_to_freq_license[i] > letter_freq_word[i]:
#                     stop = True
#                     break
#             if stop == False:
#                 res = word
#
#         return res


import heapq

class MyHeap(object):
   def __init__(self, initial=None, key=lambda x:x):
       self.key = key
       if initial:
           self._data = [key(item) for item in initial]
           heapq.heapify(self._data)
       else:
           self._data = []

   def push(self, item):
       heapq.heappush(self._data, (self.key(item), item))

   def pop(self):
       return heapq.heappop(self._data)[1]
x = MyHeap([[1,9],[2,7]])
x.push([3,4])
print(x)
