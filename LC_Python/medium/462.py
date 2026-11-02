class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        N = len(nums)

        if N % 2 == 1:
            median = nums[N // 2]
        else:
            median = (nums[N // 2] + nums[(N // 2) - 1]) // 2

        return sum([abs(x - median) for x in nums])


sol = Solution()
print(sol.minMoves2([1, 2, 3]))
print(sol.minMoves2([1, 10, 2, 9]))
print(sol.minMoves2([2, 4]))
