class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs == [] or len(costs[0]) == 0:
            return 0
        for i in range(1,len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[len(costs)-1][0], costs[len(costs)-1][1], costs[len(costs)-1][2])


class Solution1(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs == [] or len(costs[0]) == 0:
            return 0
        n = len(costs)
        f = [[0 for i in range(3)] for j in range(n)]
        f[0][0] = costs[0][0]
        f[0][1] = costs[0][1]
        f[0][2] = costs[0][2]
        for i in range(1,n):
            f[i][0] = min(f[i-1][1] + costs[i][0], f[i-1][2] + costs[i][0])
            f[i][1] = min(f[i-1][0] + costs[i][1], f[i-1][2] + costs[i][1])
            f[i][2] = min(f[i-1][0] + costs[i][2], f[i-1][1] + costs[i][2])
        return min(f[n-1][0], f[n-1][1], f[n-1][2])

if __name__ == "__main__":

    x = Solution1()
    w = [[7, 6, 2]] #2
    print x.minCost(w)
    w = [[20,18,4],[9,9,10]]
    print x.minCost(w) #13
