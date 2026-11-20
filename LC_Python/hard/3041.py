from collections import defaultdict


class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        dp = defaultdict(int)
        ans = 0

        nums.sort()

        for num in nums:
            # Bump up current element.
            dp[num + 1] = max(dp[num + 1], dp[num] + 1)

            # Use current element as-is.
            dp[num] = max(dp[num - 1] + 1, dp[num])

            ans = max(ans, dp[num], dp[num + 1])

        return ans


sol = Solution()
print(sol.maxSelectedElements([2, 1, 5, 1, 1]))
print(sol.maxSelectedElements([1, 4, 7, 10]))
