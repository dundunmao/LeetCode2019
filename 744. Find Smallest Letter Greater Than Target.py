class Solution:
    def nextGreatestLetter(self, letters, target):
        start = 0
        end = len(letters) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if letters[mid] > target:
                end = mid
            else:
                start = mid
        if letters[start] > target:
            return letters[start]
        elif letters[end] > target:
            return letters[end]
        elif letters[end] <= target:
            return letters[0]
s = Solution()
# a = ['a', 'b']
# b = 'z'
# print(s.nextGreatestLetter(a,b))
a = ["c","f","j"]
b = "j"
print(s.nextGreatestLetter(a,b))
