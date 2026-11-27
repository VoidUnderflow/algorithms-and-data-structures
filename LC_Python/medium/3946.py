from collections import Counter

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

        # dp[rem] = max number of items up to idx that leave exactly rem budget remaining
        # dp[rem] = -1 => rem is unreachable
        dp = [-1] * (budget + 1)
        dp[budget] = 0

        for idx in range(N):
            count, price = items[idx]

            for remaining_budget in range(price, budget + 1):
                if dp[remaining_budget] >= 0:
                    dp[remaining_budget - price] = max(
                        dp[remaining_budget - price], dp[remaining_budget] + count
                    )

        return max(
            dp[remaining_budget] + remaining_budget // min_price
            for remaining_budget in range(budget + 1)
            if dp[remaining_budget] >= 0
        )


sol = Solution()
print(sol.maximumSaleItems([[6, 2], [2, 6], [3, 4]], 9))
print(sol.maximumSaleItems([[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]], 8))
