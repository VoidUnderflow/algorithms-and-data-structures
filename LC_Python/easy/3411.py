from math import gcd


class Solution:
    def maxLength(self, nums: list[int]) -> int:
        ans = 2
        curr_prod = 1
        start = 0

        for end in range(len(nums)):
            while gcd(curr_prod, nums[end]) > 1:
                curr_prod = curr_prod // nums[start]
                start += 1

            curr_prod *= nums[end]
            ans = max(ans, end - start + 1)

        return ans


sol = Solution()
print(sol.maxLength([1, 2, 1, 2, 1, 1, 1]))
print(sol.maxLength([2, 3, 4, 5, 6]))
print(sol.maxLength([1, 2, 3, 1, 4, 5]))
