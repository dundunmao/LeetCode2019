class Solution:
    def maximumSwap(self, num: int) -> int:
        array = [int(ele) for ele in str(num)]
        large_array = [len(array) - 1] * len(array)
        for i in range(len(array) - 2, -1, -1):
            if array[i] > array[large_array[i + 1]]:
                large_array[i] = i
            else:
                large_array[i] = large_array[i + 1]
        for i in range(len(array)):
            if array[i] < array[large_array[i]]:
                array[i], array[large_array[i]] = array[large_array[i]], array[i]
                break
        return int(''.join([str(ele) for ele in array]))
s = Solution()
a = 2736
print(s.maximumSwap(a))
