from math import inf


class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [0]

        for idx in range(1, n + 1):
            curr_min = inf
            for prev_idx in range(idx - 3, idx):
                if prev_idx < 0:
                    continue
                curr_min = min(curr_min, (idx - prev_idx) ** 2 + dp[prev_idx])
            dp.append(curr_min + costs[idx - 1])

        print(dp)
        return dp[-1]


sol = Solution()
print(sol.climbStairs(4, [1, 2, 3, 4]))
print(sol.climbStairs(4, [5, 1, 6, 2]))
print(sol.climbStairs(3, [9, 8, 3]))
