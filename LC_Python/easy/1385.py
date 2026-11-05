from bisect import bisect_left, bisect_right


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        arr2.sort()

        for num1 in arr1:
            idx_left = bisect_left(arr2, num1 - d)
            idx_right = bisect_right(arr2, num1 + d, lo=idx_left)
            if idx_left == idx_right:
                ans += 1

        return ans


sol = Solution()
print(sol.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2))
print(sol.findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3))
print(sol.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6))
