from math import comb

MODN = 10**9 + 7


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return comb(n + k - 1, 2 * k) % MODN


sol = Solution()
print(sol.numberOfSets(4, 2))
print(sol.numberOfSets(3, 1))
print(sol.numberOfSets(30, 7))
