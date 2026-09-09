class Solution:
    def countCommas(self, n: int) -> int:
        magnitude = len(str(n)) - 1
        if magnitude < 3:
            return 0

        base_exp = magnitude - magnitude % 3
        n_commas = 0
        for exp in range(3, base_exp, 3):
            n_commas += (exp // 3) * 999 * 10**exp
        n_commas += (base_exp // 3) * (n - 10**base_exp + 1)

        return n_commas


sol = Solution()
print(sol.countCommas(1002))
print(sol.countCommas(998))
print(sol.countCommas(10_008_123_224))
print(sol.countCommas(999999999999998))
