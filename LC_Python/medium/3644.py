class Solution:
    # nums contains 0..N-1
    # k will necessarily also be in 0..N-1
    # any elem that needs to be swapped & k = k
    # => can use swaps with k to sort the array
    def sortPermutation(self, nums: list[int]) -> int:
        ans = -1
        for idx, num in enumerate(nums):
            if num != idx:
                ans &= num
        return ans if ans > 0 else 0


sol = Solution()
print(sol.sortPermutation([0, 3, 2, 1]))
print(sol.sortPermutation([0, 1, 3, 2]))
print(sol.sortPermutation([3, 2, 1, 0]))
