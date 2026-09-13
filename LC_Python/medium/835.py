from typing import List, Tuple
from collections import defaultdict


def map_ones(img: List[List[int]]) -> List[Tuple[int, int]]:
    N = len(img)
    ones = []

    for row in range(N):
        for col in range(N):
            if img[row][col] == 1:
                ones.append((row, col))

    return ones


class Solution:
    def largestOverlap(self, img_1: List[List[int]], img_2: List[List[int]]) -> int:
        ones_1 = map_ones(img_1)
        ones_2 = map_ones(img_2)

        deltas = defaultdict(int)
        for x2, y2 in ones_2:
            for x1, y1 in ones_1:
                deltas[(x2 - x1, y2 - y1)] += 1

        return max(deltas.values(), default=0)


sol = Solution()
print(
    sol.largestOverlap(
        [[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
    )
)
print(sol.largestOverlap([[1]], [[1]]))
print(sol.largestOverlap([[0]], [[0]]))
