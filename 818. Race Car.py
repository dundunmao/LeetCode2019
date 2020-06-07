class Solution:
    def racecar(self, target: int) -> int:
        visited = set()  # 存的是 (pos, speed)
        queue = collections.deque()

        queue.append((0, 1, 0))  # 存的是 (pos, speed, step)
        while len(queue) > 0:
            current = queue.popleft()
            if current[0] == target:
                return current[2]
            if abs(current[0]) >= 20000:  # 如果已经超过target的两倍了，就不往下走了，因为回头走不如从10000往前走
                continue
            # 按speed走
            if (current[0] + current[1], current[1] * 2) not in visited:
                queue.append((current[0] + current[1], current[1] * 2, current[2] + 1))
                visited.add((current[0] + current[1], current[1] * 2))
            if abs(current[1]) >= 20000:  # 如果速度超过target的2倍，走一下，距离也超过2倍
                continue
            # 掉头
            # 如果当前是正速度
            if current[1] > 0:
                if (current[0], -1) not in visited:
                    queue.append((current[0], -1, current[2] + 1))
                    visited.add((current[0], -1))
            else:
                # 如果当前是负速度
                if (current[0], 1) not in visited:
                    queue.append((current[0], 1, current[2] + 1))
                    visited.add((current[0], 1))
        return -1 
