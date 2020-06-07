from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips_object_array = []
        for ele in clips:
            clips_object_array.append(Clip(ele[0], ele[1]))
        # 按start时间sort
        clips_object_array.sort()
        # 检查第一个start是不是0
        if clips_object_array[0].start != 0:
            return -1
        # 过滤，同样的start留最大end的
        new_clip = []
        new_clip.append(clips_object_array[0])
        for i in range(1, len(clips_object_array)):
            if clips_object_array[i - 1].start != clips_object_array[i].start:
                new_clip.append(clips_object_array[i])
        # 开始接
        clip_stack = []
        clip_stack.append(new_clip[0])

        for i in range(1, len(new_clip)):
            # 先检查是不是已经到T了，到了就可以返回了
            if clip_stack[-1].end >= T:
                return len(clip_stack)
            # step 2, 把stack尾巴该pop的pop出去
            if clip_stack[-1].end < new_clip[i].end:
                while len(clip_stack) > 1 and clip_stack[-2].end >= new_clip[i].start:
                    clip_stack.pop()
                # 把新来的接进去
                clip_stack.append(new_clip[i])
            if len(clip_stack) > 1 and clip_stack[-2].end < clip_stack[-1].start:
                return -1
        # 检查end到没到T，没到就错了
        if clip_stack[-1].end < T:
            return -1
        return len(clip_stack)


class Clip:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(a, b):
        if a.start == b.start:
            return a.end > b.end
        return a.start < b.start

class Solution1:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        f = [0] * (T)
        clips.sort(key=lambda x:(x[0], -x[1]))
        for ele in clips:
            start = ele[0]
            end = min(ele[1] - 1, T - 1)
            if start >= T:
                break
            if f[end] != 0:
                continue
            min_clip = f[start - 1]
            for i in range(start, end + 1):
                if f[i] == 0:
                    f[i] = min_clip + 1
        res = 0
        for ele in f:
            if ele == 0:
                return -1
            else:
                res = max(res, ele)
        print(res)
        return res



s = Solution1()

# a = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
# t = 10
# print(s.videoStitching(a, t)) # 3

# a = [[0,2],[4,8]]
# t = 8
# print(s.videoStitching(a, t)) # -1

a = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
t = 9
print(s.videoStitching(a, t)) # 3


a = [[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]]
t = 5
print(s.videoStitching(a, t)) # 1
a = [[8,10],[17,39],[18,19],[8,16],[13,35],[33,39],[11,19],[18,35]]
t = 20
print(s.videoStitching(a, t)) # -1


