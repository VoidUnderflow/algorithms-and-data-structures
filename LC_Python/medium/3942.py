class Solution:
    def minOperations(self, nums: list[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0

        zero_idx = nums.index(0)
        asc, desc = True, True
        for ii in range(1, N):
            val = nums[(zero_idx + ii) % N]
            if val != ii:
                asc = False
            if val != N - ii:
                desc = False

            if not asc and not desc:
                return -1

        if asc:
            return min(zero_idx, N - zero_idx + 2)
        # zero_idx -> N - 1 - zero_idx + plug into above?
        # reversing is an extra op...
        return 1 + min(N - zero_idx - 1, zero_idx + 1)


sol = Solution()
print(sol.minOperations([0, 2, 1]))
print(sol.minOperations([1, 0, 2]))
print(sol.minOperations([2, 0, 1, 3]))
