class Solution:
    def longestArithSeqLength(self, A) -> int:
        diff_to_count_hash = {}
        all_result = [{} for i in range(len(A))]
        for i in range(len(A) - 2, -1, -1):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                if diff in all_result[j]:
                    new_count = all_result[j][diff] + 1
                else:
                    new_count = 2

                if diff in all_result[i]:
                    all_result[i][diff] = max(all_result[i][diff], new_count)
                else:
                    all_result[i][diff] = new_count

                if diff in diff_to_count_hash:
                    diff_to_count_hash[diff] = max(diff_to_count_hash[diff], all_result[i][diff])
                else:
                    diff_to_count_hash[diff] = all_result[i][diff]

        return max(diff_to_count_hash.values())


class Solution1:
    def longestArithSeqLength(self, A):
        n = len(A)
        array_of_hash = [{} for i in range(n)]
        res = float('-inf')
        n = len(A)
        for i in range(n - 2, -1, -1):
            diff_hash = array_of_hash[i]
            for j in range(i + 1, n):
                diff = A[j] - A[i]
                if diff in array_of_hash[j]:
                    count = array_of_hash[j][diff] + 1
                else:
                    count = 2

                if diff in diff_hash:
                    diff_hash[diff] = max(diff_hash[diff], count)
                else:
                    diff_hash[diff] = count
                res = max(res, diff_hash[diff])
        return res


s = Solution1()
# A = [44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]
# print(s.longestArithSeqLength(A))
# A = [9,4,7,2,10] # 3
# print(s.longestArithSeqLength(A))
# A = [20,1,15,3,10,5,8] # 4
# print(s.longestArithSeqLength(A))
# A = [3,6,9,12] #4
# print(s.longestArithSeqLength(A))

# A = [17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]
# A = [25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]
A = [83,20,17,43,52,78,68,45] # 2
print(s.longestArithSeqLength(A))

