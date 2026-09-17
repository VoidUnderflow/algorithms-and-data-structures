from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        N = len(arr)

        last_idx = dict()
        last_idx[0] = -1

        curr_sum = 0
        min_len_so_far = N + 1

        ans = N + 1

        for right_idx, num in enumerate(arr):
            curr_sum += num
            if curr_sum - target in last_idx:
                left_idx = last_idx[curr_sum - target]
                curr_len = right_idx - left_idx
                if left_idx != -1 and min_len_so_far != N + 1:
                    ans = min(ans, curr_len + arr[left_idx])

                min_len_so_far = min(min_len_so_far, curr_len)

            arr[right_idx] = min_len_so_far
            last_idx[curr_sum] = right_idx

        return ans if ans <= N else -1


sol = Solution()
print(sol.minSumOfLengths([3, 2, 2, 4, 3], 3))
print(sol.minSumOfLengths([7, 3, 4, 7], 7))
print(sol.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6))
