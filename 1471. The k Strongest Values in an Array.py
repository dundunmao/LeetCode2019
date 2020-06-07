class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sorted_arr = sorted(arr)
        p = (len(arr) - 1) // 2
        median = sorted_arr[p]
        res = []
        i = 0
        j = len(arr) - 1
        while i < j and k > 0:
            if abs(sorted_arr[i] - median) > abs(sorted_arr[j] - median):
                res.append(sorted_arr[i])
                i += 1
            else:
            # elif abs(arr[i] - median) <= abs(arr[j] - median):
                res.append(sorted_arr[j])
                j -= 1
            k -= 1
        if k > 0:
            res.append(sorted_arr[i])
        return res