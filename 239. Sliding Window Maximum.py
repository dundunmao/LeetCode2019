from collections import deque
class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        res = []
        if len(nums) == 0:
            return []
        for end in range(0, len(nums)):
            if len(dq) != 0 and (end - dq[0]) >= k:   #从queue里popleft的条件是queue的头与j的差等于k。
                dq.popleft()
            while len(dq) != 0 and nums[dq[-1]] < nums[end]: #每次要进一个数就要把之前比他小的都pop出去
                dq.pop()
            dq.append(end)      #pop完把他加入queue尾
            if end >= k - 1:    #从第k个开始才把队头往res里append
                res.append(nums[dq[0]])
        return res


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        index_deque = deque()
        res = []
        maxi = float('-inf')
        index_deque.append(0)
        for i in range(0, len(nums)):
            # 删尾巴
            while len(index_deque) > 0 and nums[i] >= nums[index_deque[-1]]:
                index_deque.pop()
            # 越界的头
            if len(index_deque) > 0 and index_deque[0] <= i - k:
                index_deque.popleft()
            # 加当前点
            index_deque.append(i)
            # res
            if i >= k - 1:
                res.append(nums[index_deque[0]])
        return res



if __name__ == '__main__':
    s = Solution()
    # a = "aaaabc"
    # k = 2
    #
    # print s.lengthOfLongestSubstringKDistinct1(a,k)
    # a = 'eceba'
    # k = 2
    # print s.lengthOfLongestSubstringKDistinct1(a, k)
    a = [1,-1]  #[1, -1]
    k = 1
    print s.maxSlidingWindow(a, k)
    a = [1,3,-1,-3,5,3,6,7]  #[3, 3, 5, 5, 6, 7]
    k = 3
    print s.maxSlidingWindow(a, k)
