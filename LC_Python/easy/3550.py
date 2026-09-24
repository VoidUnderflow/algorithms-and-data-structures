class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for idx, num in enumerate(nums):
            if idx == sum([int(x) for x in str(num)]):
                return idx
        return -1


sol = Solution()
print(sol.smallestIndex([1, 3, 2]))
print(sol.smallestIndex([1, 10, 11]))
print(sol.smallestIndex([1, 2, 3]))
