class Solution:
    def minmaxGasDist(self, stations, K):
            """
            :type stations: List[int]
            :type K: int
            :rtype: float
            """
            def helper(target, K):
                cnt = 0 
                for i in range(len(stations)-1):
                    cnt+=(stations[i+1]-stations[i])//target
                return cnt>K

            l, r = 0, 1e8

            delta =1e-6
            while r>=l:
                mid = (l+r)/2.0
                if helper(mid, K):
                    l = mid+delta
                else:
                    r = mid-delta
            return l        