from collections import Counter


class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        # Sort items by price.
        items.sort(key=lambda x: x[1])

        # Get frequency of each factor.
        factor_counts = Counter([x[0] for x in items])

        # factor_counts => multiple_counts
        max_factor = max(item[0] for item in items)
        for factor in range(1, max_factor + 1):
            if factor_counts[factor] == 0:
                continue

            for mult in range(factor * 2, max_factor + 1, factor):
                factor_counts[factor] += factor_counts[mult]

        ans = 0
        min_price = items[0][1]
        for factor, price in items:
            if price > 2 * min_price or price > budget:
                break

            # How many of the current item can you afford to take?
            # The max you should take is the number of multiples - 1 (excluding the current item).
            max_count = min(factor_counts[factor] - 1, budget // price)
            ans += 2 * max_count
            budget -= max_count * price

        # Spend remaining budget buying the cheapest item.
        ans += budget // min_price

        return ans


sol = Solution()
print(sol.maximumSaleItems([[1, 6], [2, 4], [3, 5]], 19))
print(sol.maximumSaleItems([[2, 8], [1, 10], [6, 6], [4, 12], [5, 20], [5, 17]], 35))
