import collections
class Solution:
    def candy(self, ratings) -> int:
        left = [1]
        right = collections.deque()
        right.appendleft(1)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left.append(left[-1] + 1)
            else:
                left.append(1)

        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                right.appendleft(right[0] + 1)
            else:
                right.appendleft(1)

        sum_up = 0
        for i in range(len(ratings)):
            sum_up += max(left[i], right[i])
        return sum_up
