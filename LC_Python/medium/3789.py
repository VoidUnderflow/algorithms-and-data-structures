class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        if costBoth > cost1 + cost2:
            return need1 * cost1 + need2 * cost2

        if costBoth < min(cost1, cost2):
            return costBoth * max(need1, need2)

        ans = costBoth * min(need1, need2)
        if need1 > need2:
            return ans + min(cost1, costBoth) * (need1 - need2)
        else:
            return ans + min(cost2, costBoth) * (need2 - need1)


sol = Solution()
print(sol.minimumCost(3, 2, 1, 3, 2))  # 3
print(sol.minimumCost(5, 4, 15, 2, 3))  # 22
print(sol.minimumCost(5, 4, 15, 0, 0))  # 0
print(sol.minimumCost(50, 55, 72, 5, 3))  # 316
print(sol.minimumCost(37, 53, 45, 5, 18))  # 810
