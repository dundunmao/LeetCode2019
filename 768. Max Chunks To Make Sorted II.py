class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res_array = []
        for i in range(len(arr)):
            if i == 0:
                res_array.append(arr[i])
                continue
            else:
                #如果新进的比最后一个小，最后一个的最大值要记录一下
                if arr[i] < res_array[-1]:
                    maxi = res_array[-1]
                    start = len(res_array) - 2
                    #开始用新进的跟倒数第二个，以及他之前的比，只要小，这个的最大值就设为之前记录那个，在把尾巴的这个给删了
                    while start >= 0 and res_array[start] > arr[i]:
                        res_array[start] = maxi
                        del res_array[-1]
                        start -= 1
                else:
                    res_array.append(arr[i])
        return len(res_array)
