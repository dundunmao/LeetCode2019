# There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. They all look the same. If a pig drinks that poison it will die within 15 minutes. What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.
#
# Answer this question, and write an algorithm for the follow-up general case.
#
# Follow-up:
#
# If there are n buckets and a pig drinking poison will die within m minutes, how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.

# 1000桶水，最少几只猪可以试出来哪桶水有毒，猪喝完水15分钟后死了说明有毒。总共给一个小时时间。
import math
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        times = minutesToTest/minutesToDie
        number_of_pig = 0
        while buckets > 1:
            number_of_pig += 1
            rest = buckets%times
            buckets = math.ceil(buckets/float(times))

        if rest > 0:
            number_of_pig += 1
        return number_of_pig

if __name__ == '__main__':
    s = Solution()
    a = [1,1,1,1,1]
    X = 3
    print s.poorPigs(1000,12,60)
