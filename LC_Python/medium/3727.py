class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums = [abs(x) for x in nums]
        nums.sort()

        ans, idx = 0, 0
        while idx < len(nums):
            if idx == len(nums) - 1:
                ans += nums[-1] ** 2
                break

            ans = ans + nums[-1] ** 2 - nums[idx] ** 2
            idx += 1
            nums.pop()

        return ans


sol = Solution()
print(sol.maxAlternatingSum([1, 2, 3]))
print(sol.maxAlternatingSum([1, -1, 2, -2, 3, -3]))
