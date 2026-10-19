class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        same, lower = 0, 0
        for num in nums:
            if num < target:
                lower += 1
            elif num == target:
                same += 1

        return list(range(lower, same + lower))


sol = Solution()
print(sol.targetIndices([1, 2, 5, 2, 3], 2))
print(sol.targetIndices([1, 2, 5, 2, 3], 3))
print(sol.targetIndices([1, 2, 5, 2, 3], 5))
