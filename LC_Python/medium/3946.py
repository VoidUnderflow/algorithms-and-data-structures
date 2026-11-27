from collections import Counter
from functools import cache

MAX_FACTOR = MAX_PRICE = 1500


class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        N = len(items)
        factor_counts = Counter([x[0] for x in items])
        min_price = MAX_PRICE + 1

        for idx in range(N):
            factor, price = items[idx]

            min_price = min(min_price, price)

            curr_count = factor_counts[factor]
            multiple = 2 * factor

            while multiple <= MAX_FACTOR:
                curr_count += factor_counts[multiple]
                multiple += factor

            items[idx][0] = curr_count

        @cache
        def dp(idx: int, remaining_budget: int) -> int:
            if idx == N:
                return remaining_budget // min_price

            skip = dp(idx + 1, remaining_budget)
            if items[idx][1] > remaining_budget:
                return skip
            return max(
                skip,
                items[idx][0] + dp(idx + 1, remaining_budget - items[idx][1]),
            )

        return dp(0, budget)


sol = Solution()
print(sol.maximumSaleItems([[6, 2], [2, 6], [3, 4]], 9))
print(sol.maximumSaleItems([[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]], 8))
