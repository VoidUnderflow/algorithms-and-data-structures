from collections import Counter


class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        N = len(nums)

        # We map windows of nums with lengths = powers of two to unique ids.
        window_size = 1

        # window_id[pow][idx] = id of window nums[idx:(idx + 2**k)]
        window_id = [nums]
        while window_size * 2 <= N:
            prev_pow_ids = window_id[-1]
            pair_to_ids = {}
            curr_pow_ids = []

            for idx in range(len(prev_pow_ids) - window_size):
                curr_pair = (prev_pow_ids[idx], prev_pow_ids[idx + window_size])

                if curr_pair not in pair_to_ids:
                    pair_to_ids[curr_pair] = len(pair_to_ids)

                curr_pow_ids.append(pair_to_ids[curr_pair])

            window_id.append(curr_pow_ids)
            window_size *= 2

        def has_unique_window(window_size: int) -> bool:
            log = window_size.bit_length() - 1
            block_size = 2**log
            curr_pow_ids = window_id[log]

            # Concatenate ids of block starting at the first element and ending at the last element
            # of the current window.
            curr_ids = Counter(
                (curr_pow_ids[idx], curr_pow_ids[idx + window_size - block_size])
                for idx in range(N - window_size + 1)
            )

            return 1 in curr_ids.values()

        # Simple binary search.
        # If there's a unique window of length i, any subsequence of length > 1 that includes it
        # will also be unique.
        left, right = 1, N
        while left < right:
            mid = (left + right) // 2
            if has_unique_window(mid):
                right = mid
            else:
                left = mid + 1

        return left


sol = Solution()
print(sol.smallestUniqueSubarray([3, 3, 3]))
print(sol.smallestUniqueSubarray([2, 1, 2, 3, 3]))
print(sol.smallestUniqueSubarray([1, 1, 2, 2, 1]))
