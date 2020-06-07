from typing import List


class Solution:
	def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
		l = 0
		for i in range(n):
			if leftChild[i] != -1:
				l += 1
			if rightChild[i] != -1:
				l += 1
			if leftChild[i] == 0 or rightChild[i] == 0:
				if leftChild[-1] != 0 and rightChild[-1] != 0:
					return False
		if l != n - 1:
			return False
		return True