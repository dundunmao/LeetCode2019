class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs == [] or len(costs) == 0:
            return 0
        n = len(costs)
        k = len(costs[0])

        pre1, pre2,min1 = -1, -1, 0
        for i in range(0,n):
            for j in range(k):
                if j != pre1:  #上一轮最小的不是j色，就用这个最小的
                    if pre1 >= 0:
                        costs[i][j] += costs[i-1][pre1]
                else:
                    if pre2 >= 0: #上一轮最小的是j色，就用这个第二小的
                        costs[i][j] += costs[i-1][pre2]
            #求这一轮的第一小和第二小cost的对应的颜色
            min1, min2 = 0,0
            for j in range(1,k):
                if costs[i][j] < costs[i][min1]:
                    min2 = min1
                    min1 = j
                elif costs[i][j] < costs[i][min2]:
                    min2 = j
            pre1 = min1
            pre2 = min2
        return  costs[n-1][min1]

class Solution1(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs == [] or len(costs[0]) == 0:
            return 0
        n = len(costs)
        k = len(costs[0])
        for i in range(1,n):
            for j in range(0,k):  #当i房子涂j色时
                mini = float('inf')
                for m in range(0,k):  #i-1房子涂除j以外的颜色，取最小那个
                    if m != j:
                        mini = min(mini, costs[i-1][m])
                costs[i][j] += mini  #把i-1的房子cost最小的累加+ i房子涂j色的cost，就是累加到i时，涂j色的累加cost最小
        return min(costs[n-1])


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        min1 = 0
        min2 = 0
        index = float('inf')
        row = len(costs)
        col = len(costs[0])
        for i in range(row):
            # initial values
            min1_row = float('inf')
            min2_row = float('inf')
            index_row = 0
            for j in range(col):
                if j != index:
                    cost = costs[i][j] + min1
                else:
                    cost = costs[i][j] + min2

                # insertion sort
                if cost <= min2_row:
                    min2_row = cost
                if cost < min1_row:
                    min1_row, min2_row = min2_row, min1_row
                    index_row = j
                # sort end
            min1 = min1_row
            min2 = min2_row
            index = index_row
        return min1


if __name__ == "__main__":

    x = Solution1()
    w = [[7,19,11,3,7,15,17,5,6,18,1,15,18,11],[13,18,18,8,13,12,11,13,4,8,2,4,5,20],[14,5,18,4,7,6,1,6,11,6,16,6,13,17],[18,17,11,3,12,4,8,6,2,7,10,9,19,3],[4,3,2,14,11,15,18,1,17,1,6,14,14,9],[9,13,15,14,5,1,1,6,11,15,16,12,10,18],[19,2,11,3,13,4,13,7,16,16,20,18,20,8],[8,19,20,9,18,13,17,1,2,4,3,20,15,9],[9,10,11,6,14,20,4,1,5,15,13,10,13,5],[13,11,9,11,9,16,3,19,1,11,6,7,12,13],[14,1,15,14,11,12,7,14,12,11,6,9,5,5]]
    #17
    print(x.minCostII(w))
    w = [[20,18,4],[9,9,10]]
    print(x.minCostII(w)) #13
