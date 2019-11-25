class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        res = 0
        group = {}
        for ele in answers:
            if ele in group:
                group[ele] +=1
            else:
                group[ele] = 1
        for ans, num in group.items():
            if num % (ans + 1) == 0:
                res += num / (ans+1) * (ans+1)
            else:
                res += (num / (ans+1) + 1) * (ans+1)
        return res
