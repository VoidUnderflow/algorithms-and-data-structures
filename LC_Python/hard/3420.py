from heapq import heappush, heappop


class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        N = len(nums)

        n_ops = 0  # nr. of ops to make current window non-decreasing
        max_heap = []  # window maximum
        next_greater = (
            [N] * N
        )  # next_greater[ii] = jj => nums[jj] is the next greater element for nums[ii];
        rev_former_greater = [
            [] for _ in range(N)
        ]  # rev_former_greater[idx] = [i1, i2 ,i3] => nums[idx] is the next greater element to the left of each nums[i1], nums[i2], nums[i3]
        stack = []  # decreasing monotonic stack (contains indices)

        ans = 0
        left_idx = 0
        for right_idx in range(N):
            # Maintain stack invariant & update next_greater.
            while len(stack) > 0 and nums[right_idx] >= nums[stack[-1]]:
                next_greater[stack[-1]] = right_idx
                stack.pop()

            # nums[stack[-1]] is the nearest greater left element for nums[right_idx]
            if len(stack) > 0:
                rev_former_greater[stack[-1]].append(right_idx)
            stack.append(right_idx)

            # update the max heap
            heappush(max_heap, ((-nums[right_idx], right_idx)))

            # update ops
            n_ops += abs(-max_heap[0][0] - nums[right_idx])

            # while n_ops > k, shrink the window
            while n_ops > k:
                for idx in rev_former_greater[left_idx]:
                    n_ops -= (nums[left_idx] - nums[idx]) * (
                        min(right_idx + 1, next_greater[idx]) - idx
                    )
                left_idx += 1

                # maintain heap invariant
                while max_heap and max_heap[0][1] < left_idx:
                    heappop(max_heap)

            ans += right_idx - left_idx + 1

        return ans


sol = Solution()

print(sol.countNonDecreasingSubarrays([6, 3, 1, 2, 4, 4], 7))  # 17
print(sol.countNonDecreasingSubarrays([6, 3, 1, 3, 6], 4))  # 12
