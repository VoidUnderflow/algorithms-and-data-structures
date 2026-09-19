class Solution:
    def checkOverlap(
        self,
        radius: int,
        x_center: int,
        y_center: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        x_closest = x1 if x_center <= x1 else x2 if x_center >= x2 else x_center
        y_closest = y1 if y_center <= y1 else y2 if y_center >= y2 else y_center
        return (x_closest - x_center) ** 2 + (y_closest - y_center) ** 2 <= radius**2


sol = Solution()
print(sol.checkOverlap(1, 0, 0, 1, -1, 3, 1))
print(sol.checkOverlap(1, 1, 1, 1, -3, 2, -1))
print(sol.checkOverlap(1, 0, 0, -1, 0, 0, 1))
print(sol.checkOverlap(1, 1, 1, -3, -3, 3, 3))
