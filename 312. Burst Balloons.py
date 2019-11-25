class Solution1(object):
    """
    @param {int[]} nums a list of integer
    @return {int} an integer, maximum coins
    """
    def maxCoins(self, nums):
        # Write your code here
        n = len(nums)
        f = [[0 for i in range(n + 2)] for j in range(n + 2)]
        visit = [[0 for i in range(n + 2)] for j in range(n + 2)]
        nums.append(1)
        nums.insert(0,1)
        return self.search(nums,f,visit,1,n)
    def search(self,arr,f,visit,left,right):
        if visit[left][right] == 1:
            return f[left][right]
        res = 0
        for k in range(left,right+1):
            mid_value = arr[left-1]*arr[k]*arr[right+1]
            left_value = self.search(arr,f,visit,left,k-1)
            right_value = self.search(arr,f,visit,k+1,right)
            res = max(res,left_value+mid_value+right_value)
        visit[left][right] = 1
        f[left][right] = res
        return res

class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return {int} an integer, maximum coins
    """
    def maxCoins(self, nums):

        nums.append(1)
        nums.insert(0,1)
        n = len(nums)
        f = [[0 for i in range(n)] for j in range(n)]
        for dis in range(2,n):
            for left in range(0, n-dis):
                right = left + dis
                for i in range(left+1, right):
                    f[left][right] = max(f[left][right], nums[i]*nums[left]*nums[right]+ f[left][i] + f[i][right])
        return f[0][n-1]

if __name__ == "__main__":
    s = Solution()
    A = [3,1,5,8] #167
    print(s.maxCoins(A))
