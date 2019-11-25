import heapq
class Solution:
    def scheduleCourse(self, courses):
        courses_sorted = []
        for ele in courses:
            courses_sorted.append(Course(ele[0], ele[1]))
        courses_sorted.sort(key=lambda x: (x.deadline, x.consume))
        res_heap = []
        start = courses_sorted[0].consume
        count = 1
        heapq.heappush(res_heap, courses_sorted[0])
        for i in range(1, len(courses_sorted)):
            cur = courses_sorted[i]
            if cur.consume + start <= cur.deadline:
                heapq.heappush(res_heap, cur)
                start = cur.consume + start
                count += 1
            else:
                if res_heap[0].consume > cur.consume:
                    start -= res_heap[0].consume - cur.consume
                    heapq.heappop(res_heap)
                    heapq.heappush(res_heap, cur)

        return count


class Course:
    def __init__(self, consume, deadline):
        self.consume = consume
        self.deadline = deadline

    def __lt__(a, b):
        return a.consume > b.consume
s = Solution()
# a = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# s.scheduleCourse(a)

# a = [[5,5],[4,6],[2,6]]
# print(s.scheduleCourse(a))
a = [[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]
print(s.scheduleCourse(a))

