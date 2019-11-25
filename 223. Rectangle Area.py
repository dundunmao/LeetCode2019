class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:

        areaA = (C - A) * (D - B)
        areaB = (G - E) * (H - F)

        left = max(A, E)
        right = min(C, G)
        top = min(D, H)
        bottom = max(B, F)

        overlap = 0
        if right > left and top > bottom:
            overlap = (right - left) * (top - bottom)

        return areaA + areaB - overlap
