
import heapq
class ExamRoom:

    def __init__(self, N: int):
        self.heap_seat = []  # heap
        self.index_to_linkedlist_node = {}
        # self.start_to_node = {}
        self.head = Double_Linked_list(-1)
        self.tail = Double_Linked_list(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.N = N

    def seat(self) -> int:
        if len(self.heap_seat) == 0:
            # in heap
            heap_node = Node(0, float('-inf'))
            heapq.heappush(self.heap_seat, heap_node)
            # in linkedlist
            linked_list_node = Double_Linked_list(0)
            self.index_to_linkedlist_node[0] = linked_list_node
            self.insert_node(self.head, self.tail, linked_list_node)
            return 0
        elif len(self.heap_seat) == 1:
            # in heap
            heap_node = Node(0, self.N - 1)
            heapq.heappush(self.heap_seat, heap_node)
            # in linkedlist
            linked_list_node = Double_Linked_list(self.N - 1)
            self.index_to_linkedlist_node[self.N - 1] = linked_list_node
            start = self.index_to_linkedlist_node[0]
            self.insert_node(start, self.tail, linked_list_node)
            return self.N - 1
        else:
            # in heap
            while self.heap_seat[0].dist <= 1:
                node = heapq.heappop(self.heap_seat)
            new_dis = node.dist // 2
            cur1 = Node(node.start, node.start + new_dis)
            cur2 = Node(node.start + new_dis, node.end)
            heapq.heappush(self.heap_seat, cur1)
            heapq.heappush(self.heap_seat, cur2)

            # in linkedlist
            mid = Double_Linked_list(node.start + new_dis)
            self.index_to_linkedlist_node[node.start + new_dis] = mid
            start = self.index_to_linkedlist_node[node.start]
            end = self.index_to_linkedlist_node[node.end]
            self.insert_node(start, end, mid)
            return cur2.start

    def insert_node(self, start, end, mid):
        start.next = mid
        mid.next = end
        end.pre = mid
        mid.pre = start

    def leave(self, p: int) -> None:
        cur_linkedlist_node = self.index_to_linkedlist_node[p]
        pre_linkedlist_node = cur_linkedlist_node.pre
        if pre_linkedlist_node == self.head:
            heapq.heappop(self.heap_seat)
            self.head.next = self.tail
            self.tail.pre = self.head
            return
        # in linked list
        pre_linkedlist_node.next = cur_linkedlist_node.next
        cur_linkedlist_node.next.pre = pre_linkedlist_node
        # in heap
        pre_pos = pre_linkedlist_node.val
        pre_heap_node = None
        cur_heap_node = None
        for i in range(len(self.heap_seat)):
            if self.heap_seat[i].start == p:
                cur_heap_node = self.heap_seat[i]
                cur_heap_index = i
            elif self.heap_seat[i].start == pre_pos:
                pre_heap_node = self.heap_seat[i]
        # update pre
        pre_heap_node.end = cur_heap_node.end
        pre_heap_node.dist = pre_heap_node.end - pre_heap_node.start
        # delete cur
        self.heap_seat[cur_heap_index], self.heap_seat[0] = self.heap_seat[0], self.heap_seat[cur_heap_index]
        heapq.heappop(self.heap_seat)
        # heapify
        heapq.heapify(self.heap_seat)


class Node:
    def __init__(self, start, end):
        self.start = start
        self.dist = end - start
        self.end = end

    def __lt__(a, b):
        if a.dist == b.dist or abs(a.dist - b.dist) == 1 and (a.dist ):
            return a.start < b.start
        return a.dist > b.dist


class Double_Linked_list:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None
# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(10)
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.seat())
# print(obj.leave(4))
# print(obj.seat())
from heapq import heappop, heappush


class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.N = N
        self.heap = []
        self.avail_first = {}
        self.avail_last = {}
        self.put_segment(0, self.N - 1)

    def put_segment(self, first, last):

        if first == 0 or last == self.N - 1:
            priority = last - first
        else:
            priority = (last - first) // 2

        segment = [-priority, first, last, True]

        self.avail_first[first] = segment
        self.avail_last[last] = segment

        heappush(self.heap, segment)

    def seat(self):
        """
        :rtype: int
        """
        while True:
            _, first, last, is_valid = heappop(self.heap)

            if is_valid:
                del self.avail_first[first]
                del self.avail_last[last]
                break

        if first == 0:
            ret = 0
            if first != last:
                self.put_segment(first + 1, last)

        elif last == self.N - 1:
            ret = last
            if first != last:
                self.put_segment(first, last - 1)

        else:
            ret = first + (last - first) // 2

            if ret > first:
                self.put_segment(first, ret - 1)

            if ret < last:
                self.put_segment(ret + 1, last)

        return ret

    def leave(self, p):
        """
        :type p: int
        :rtype: void
        """
        first = p
        last = p

        left = p - 1
        right = p + 1

        if left >= 0 and left in self.avail_last:
            segment_left = self.avail_last.pop(left)
            segment_left[3] = False
            first = segment_left[1]

        if right < self.N and right in self.avail_first:
            segment_right = self.avail_first.pop(right)
            segment_right[3] = False
            last = segment_right[2]

        self.put_segment(first, last)
obj = ExamRoom(4)
print(obj.seat())
print(obj.seat())
print(obj.seat())
print(obj.seat())
print(obj.leave(1))
print(obj.leave(3))
