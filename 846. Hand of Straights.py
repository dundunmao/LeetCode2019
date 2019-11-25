import heapq
class Group:
    def __init__(self):
        self.size = 0
        self.end = -1
class Solution:
    def isNStraightHand(self, hand, W):
        if len(hand) % W:
            return False
        num_of_group = len(hand) // W
        heapq.heapify(hand)
        groups = [Group() for i in range(num_of_group)]
        while len(hand) > 0:
            cur = heapq.heappop(hand)
            flag = False
            for ele in groups:
                if ele.size > 0 and ele.size < W and ele.end + 1 == cur:
                    ele.size += 1
                    ele.end = cur
                    flag = True
                    break
                elif ele.size == 0:
                    ele.size += 1
                    ele.end = cur
                    flag = True
                    break
            if flag == False:
                return False

        return flag == True


import heapq

class Solution1:
    def isNStraightHand(self, hand, W):
        if len(hand) % W:
            return False
        num_of_group = len(hand) // W
        num_to_freq = {}
        heap = []
        heapq.heapify(heap)
        for ele in hand:
            if ele in num_to_freq:
                num_to_freq[ele] += 1
            else:
                num_to_freq[ele] = 1
                heapq.heappush(heap, ele)

        j = num_of_group
        while len(heap) > 0 and j >= 0:
            while len(heap) > 0 and num_to_freq[heap[0]] == 0:
                heapq.heappop(heap)
            if len(heap) == 0:
                return j == 0
            start = heap[0]

            for i in range(W):
                if start not in num_to_freq or num_to_freq[start] == 0:
                    return False
                num_to_freq[start] -= 1
                start += 1

            j -= 1

        if len(heap) > 0 or j != 0:
            return False
        return True

hand = [1,2,3,4,5]

W = 4
x = Solution1()
print(x.isNStraightHand(hand,W))
