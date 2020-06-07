import collections
import string
from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        """
        :param votes:
        :return:
        """
        bucket = collections.defaultdict(str)
        # index -> alpha
        alpha_tables = {}
        for index, alpha in enumerate(string.ascii_lowercase):
            alpha_tables[index] = alpha
        for vote in votes:
            for index, team in enumerate(vote):
                bucket[team] += str(alpha_tables[index])
		# set the sort rules
        result = sorted(bucket.items(), key=lambda x: (sorted(x[1]), x[0]))
        return "".join(list(map(lambda x: x[0], result)))