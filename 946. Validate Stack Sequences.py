class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) == 0 or len(popped) == 0:
            return True
        stack = []
        i = 0

        for ele in pushed:
            stack.append(ele)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return not stack

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) == 0 or len(popped) == 0:
            return True
        pushed_deque = collections.deque()
        poped_deque = collections.deque(popped)
        pushed_deque.append(pushed[0])
        i = 0
        while len(pushed_deque) >= 0 and i < len(pushed):
            if len(pushed_deque) > 0 and pushed_deque[-1] == poped_deque[0]:
                pushed_deque.pop()
                poped_deque.popleft()
            else:
                if i + 1 < len(pushed):
                    i += 1
                    pushed_deque.append(pushed[i])
                else:
                    break
        return len(pushed_deque) == 0 and len(poped_deque) == 0
