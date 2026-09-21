class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        N = len(nums)

        # dp[mod][idx] = number of subarrays ending at idx whose product mod k is "mod"
        dp = [[0 for _ in range(N)] for _ in range(k)]
        dp[nums[0] % k][0] = 1

        for idx in range(1, N):
            curr_mod = nums[idx] % k
            dp[curr_mod][idx] += 1
            for prev_mod in range(k):
                dp[(curr_mod * prev_mod) % k][idx] += dp[prev_mod][idx - 1]

        return [sum(dp[mod]) for mod in range(k)]


sol = Solution()
print(sol.resultArray([1, 2, 3, 4, 5], 3))
print(sol.resultArray([1, 2, 4, 8, 16, 32], 4))
print(sol.resultArray([1, 1, 2, 1, 1], 2))
