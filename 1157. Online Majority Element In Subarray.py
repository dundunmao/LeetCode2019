class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.arr_set = set(arr)
        self.arr_hash_prefixt = {}
        for ele in self.arr_set:
            self.arr_hash_prefixt[ele] = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            for key, val in self.arr_hash_prefixt.items():
                if key == arr[i]:
                    val[i + 1] += val[i] + 1
                else:
                    val[i + 1] += val[i]
            # freq = self.arr_hash_prefixt[arr[i]][-1]
            # self.arr_hash_prefixt[arr[i]][i + 1] = freq + 1
            # self.arr_hash_prefixt[i] = arr_hash.copy()

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        # if left == 0:
        #     first = self.init_arr_hash
        # else:
        #     first = self.arr_hash_prefixt[left - 1]
        # second = self.arr_hash_prefixt[right]

        for ele in self.arr_set:
            if self.arr_hash_prefixt[ele][right + 1] - self.arr_hash_prefixt[ele][left] >= threshold:
                return ele
        return -1
a = [1,1,2,2,1,1]
s = MajorityChecker(a)
print(s.query(0,5,4))
print(s.query(0,3,3))
print(s.query(2,3,2))
