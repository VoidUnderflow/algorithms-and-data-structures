from math import comb

MODN = 10**9 + 7


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def count(arr: list[int]) -> int:
            if len(arr) < 3:
                return 1

            left = []
            right = []
            for num in arr[1:]:
                if num > arr[0]:
                    right.append(num)
                else:
                    left.append(num)

            return comb(len(arr) - 1, len(left)) * count(left) * count(right) % MODN

        return count(nums) - 1


sol = Solution()
print(sol.numOfWays([2, 1, 3]))
print(sol.numOfWays([3, 4, 5, 1, 2]))
print(sol.numOfWays([1, 2, 3]))
