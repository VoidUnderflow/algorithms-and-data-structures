class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        sum_to_idx = dict()
        curr_sum = 0
        for idx, num in enumerate(nums):
            curr_sum += num
            if curr_sum not in sum_to_idx:
                sum_to_idx[curr_sum] = idx

        N = len(nums)
        min_ops = sum_to_idx[x] + 1 if x in sum_to_idx else N + 1
        for idx in range(N - 1, -1, -1):
            x -= nums[idx]
            if x < 0:
                break

            if x == 0:
                min_ops = min(min_ops, N - idx)

            if x in sum_to_idx and sum_to_idx[x] < idx:
                min_ops = min(min_ops, N - idx + sum_to_idx[x] + 1)

        return min_ops if min_ops < N + 1 else -1


sol = Solution()
print(sol.minOperations([1, 1, 4, 2, 3], 5))
print(sol.minOperations([5, 6, 7, 8, 9], 4))
print(sol.minOperations([3, 2, 20, 1, 1, 3], 10))
