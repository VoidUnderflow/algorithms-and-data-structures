from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1_bl, y1_bl, x1_tr, y1_tr = rec1
        x2_bl, y2_bl, x2_tr, y2_tr = rec2

        return (
            min(x1_tr, x2_tr) - max(x1_bl, x2_bl) > 0
            and min(y1_tr, y2_tr) - max(y1_bl, y2_bl) > 0
        )
