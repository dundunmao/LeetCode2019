class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = 0
        need = 0
        sum = 0
        n = len(gas)
        for i in range(n):
            diff = gas[i] - cost[i]
            if sum + diff >= 0:
                sum += diff
            else:
                # need为之前0~i欠的，记录下这个，当start=i+1,然后算到n时，0~i就不用重新算了
                need -= sum + diff
                sum = 0  #sum 重新计算
                start = i + 1 #累加为负，0~i都不是start，start重新定位
        if start == n or sum < need:#start == n说明到最后都buxi那个，sum < need说明后面累加的不够之前欠的。
            return -1
        return start
