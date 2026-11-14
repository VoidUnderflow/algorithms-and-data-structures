class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])

        ans = float("inf")
        N = len(nums)
        for length in range(l, r + 1):
            for ii in range(N - length + 1):
                curr_sum = prefix_sum[ii + length] - prefix_sum[ii]

                if 0 < curr_sum < ans:
                    ans = curr_sum

        return -1 if ans == float("inf") else ans


sol = Solution()
print(sol.minimumSumSubarray([3, -2, 1, 4], 2, 3))
print(sol.minimumSumSubarray([-2, 2, -3, 1], 2, 3))
print(sol.minimumSumSubarray([1, 2, 3, 4], 2, 4))
