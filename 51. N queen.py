
# ]
class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens.
    @return: All distinct solutions.
    """

    def solveNQueens(self, n):
        # write your code here
        num = n
        results = []
        cols = {}
        row = 0
        self.search(row, num, results, cols)
        return results

    def search(self, row, num, results, cols):
        # if row == num:#定好一个col,row就开始从0遍历,没走一个row,col从0遍历,一旦col遍历到头,就证明尝试失败.
        if len(cols) == num:
            result = []
            for i in range(num):
                r = ['.'] * num
                r[cols[i]] = 'Q'
                result.append(''.join(r))
            results.append(result)
            return
        for col in range(num):
            if col in cols:
                continue
            if self.attack(row, col, cols):
                continue
            cols[col] = row
            self.search(row + 1, num, results, cols)
            del cols[col]

    def attack(self, row, col, cols):
        for c, r in cols.items():
            if c - r == col - row or c + r == col + row:
                return True
        return False
# 我的方法
class Solution1(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        hash = {}
        row = 0
        self.helper(n, row, hash, res)
        return res
    def helper(self,n, row, hash, res):
        if len(hash) == n:
            string  = ['']*n
            for col,row in hash.items():
                s = ('.'*col + 'Q' + '.'*(n-col-1))
                string[row] = s
            res.append(string[:])
            return
        for col in range(n):
            if col in hash:
                continue
            if self.attack(col, row, hash):
                continue
            hash[col] = row
            self.helper(n, row+1, hash, res)
            hash.pop(col)

    def attack(self, col, row, hash):
        for c, r in hash.items():
            if c+r == col +row or r - c ==  row - col:
                return True
        return False
if __name__ == '__main__':
    n=4
    s = Solution()
    print s.solveNQueens(n)
