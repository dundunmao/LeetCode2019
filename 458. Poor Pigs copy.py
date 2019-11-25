import math
class Solution(object):
#     unique id
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        times = minutesToTest/minutesToDie +1

        return int(math.ceil(math.log(buckets, times)))