class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        i = m - 1
        j = n - 1
        k = len(nums1)-1
        if k < i + j:
            return False

        while i > -1 and j > -1:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
        if j != -1:
            while j > -1:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

class Solution1(object):
    def merge(self, a, b):
        n = len(a)
        m = len(b)
        if n == 0:
            return b
        if m == 0:
            return a
        i = 0
        j = 0
        res = []
        flag = 'b' # last round from which array
        while i < n and j < m:
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
                flag = 'a'
            elif a[i] > b[j]:
                res.append(b[j])
                j += 1
                flag = 'b'
            else:
                if flag == 'b':
                    res.append(a[i])
                    i += 1
                    flag = 'a'
                else:
                    res.append(b[j])
                    j += 1
                    flag = 'b'
        if i < n:
            while i < n:
                res.append(a[i])
                i += 1
        elif j < m:
            while j < m:
                res.append(b[j])
                j += 1
        return res



if __name__ == "__main__":
    a = [1,2,3]
    b = [2,5,5]
    s = Solution1()
    print(s.merge(a, b))
    # nums1 = [1,0]
    # m = 1
    # nums2 = [2]
    # n = 1
    # s = Solution()
    # print(s.merge(nums1, m, nums2, n))
