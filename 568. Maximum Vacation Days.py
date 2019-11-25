# class Solution:
#     def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
#         memo = [[float('-inf') for j in range(len(days[0]))] for i in range(len(flights))]
#         return self.dfs(flights, days, 0, 0, memo)
#
#     # 从cur_city城市起飞，从第weekno周开始往下过，得到最大vacation
#     def dfs(self, flights, days, cur_city, weekno, memo):
#         # 如果超过最后一周了
#         if weekno == len(days[0]):
#             return 0
#         if memo[cur_city][weekno] != float('-inf'):
#             return memo[cur_city][weekno]
#
#         max_vac = 0
#         for i in range(len(flights)):
#             # 从cur_city飞到第i城市，在i市呆第weekno周，得到的假期的最大值
#             if flights[cur_city][i] == 1 or i == cur_city:
#                 # 在第i个城市过第weekno周，以及往下递归，得到的vacation，最后取最大
#                 vac = days[i][weekno] + self.dfs(flights, days, i, weekno + 1, memo)
#                 max_vac = max(max_vac, vac)
#         memo[cur_city][weekno] = max_vac
#         return max_vac
#
#
# class Solution:
#     def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
#         # N个city，K周
#         week_num = len(days[0])
#         flight_num = len(flights)
#         dp = [[float('-inf') for j in range(week_num)] for i in range(flight_num)]
#
#         for week in range(week_num):
#             for city in range(flight_num):
#                 vacation = dp[city][week]
#                 if flights[i][j] == 1 or
#
#         return self.dfs(flights, days, 0, 0, memo)
#
#     # 从cur_city城市起飞，从第weekno周开始往下过，得到最大vacation
#     def dfs(self, flights, days, cur_city, weekno, memo):
#         # 如果超过最后一周了
#         if weekno == len(days[0]):
#             return 0
#         if memo[cur_city][weekno] != float('-inf'):
#             return memo[cur_city][weekno]
#
#         max_vac = 0
#         for i in range(len(flights)):
#             # 从cur_city飞到第i城市，在i市呆第weekno周，得到的假期的最大值
#             if flights[cur_city][i] == 1 or i == cur_city:
#                 # 在第i个城市过第weekno周，以及往下递归，得到的vacation，最后取最大
#                 vac = days[i][weekno] + self.dfs(flights, days, i, weekno + 1, memo)
#                 max_vac = max(max_vac, vac)
#         memo[cur_city][weekno] = max_vac
#         return max_vac


class Solution:
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """

        n_city, n_week = len(days), len(days[0])
        #表示在i这个城市呆的第j周，到目前为止最大vacation
        dp = [[-1] * n_week for _ in range(n_city)]
        # 第0城市到第city城市有航班没
        for city, reachable in enumerate(flights[0]):
            if reachable or city == 0:
                #从第0城市出发，到第city这个城市呆第0周
                dp[city][0] = days[city][0]

        # calculate `dp` week by week. The end is n_week - 1 because at that week we updated
        #    the last week's status
        for week in range(n_week - 1):
            for city in range(len(dp)):
                vacation = dp[city][week]
                if vacation < 0:  # use -1 to indicate an not-reachable-yet city.
                    continue

                # 当前city过第week周的vacation=下一个city过第week+1
                for next_city, reachable in enumerate(flights[city]):
                    if reachable or next_city == city:
                        # 下一个city过下一周累计值 = 当前city过当前周的累计 + days[next_city][week + 1]
                        dp[next_city][week + 1] = max(dp[next_city][week + 1],
                                                      dp[city][week] + days[next_city][week + 1])

        return max([ele[-1] for ele in dp]) # return the max value of the last column

s = Solution()
# flights = [[0,1,1],[1,0,1],[1,1,0]]
# days = [[1,3,1],[6,0,3],[3,3,3]]
# print(s.maxVacationDays(flights, days))
flights = [[0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
days = [[0,0,7,0],[2,0,0,7],[7,7,7,7],[7,7,7,7]]
print(s.maxVacationDays(flights, days))
