class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums_sum, max_num = 0, 0
        for num in nums:
            nums_sum += num
            max_num = max(max_num, num)

        return len(nums) * max_num - nums_sum


sol = Solution()
print(sol.minMoves([1, 2, 3]))
print(sol.minMoves([4, 4, 5]))
