from heapq import heappush, heappop
from collections import defaultdict
from math import inf


class RollingMedian:
    def __init__(self):
        self.left_heap = []
        self.right_heap = []

        self.sum_left = 0
        self.sum_right = 0

        self.left_size = 0
        self.right_size = 0

        self.lazy_removal = defaultdict(int)

    def prune(self, heap: list[int], sign: int) -> None:
        while heap and self.lazy_removal[heap[0] * sign] > 0:
            self.lazy_removal[heap[0] * sign] -= 1
            heappop(heap)

    def balance_heaps(self) -> None:
        self.prune(self.left_heap, -1)
        self.prune(self.right_heap, 1)

        if self.left_size > self.right_size + 1:
            num = -heappop(self.left_heap)
            heappush(self.right_heap, num)

            self.sum_right += num
            self.sum_left -= num

            self.right_size += 1
            self.left_size -= 1

            self.prune(self.left_heap, -1)
        elif self.right_size > self.left_size:
            num = heappop(self.right_heap)
            heappush(self.left_heap, -num)

            self.sum_left += num
            self.sum_right -= num

            self.left_size += 1
            self.right_size -= 1

            self.prune(self.right_heap, 1)

    def add(self, num: int) -> None:
        if not self.left_heap or num <= -self.left_heap[0]:
            heappush(self.left_heap, -num)
            self.left_size += 1
            self.sum_left += num
        else:
            heappush(self.right_heap, num)
            self.right_size += 1
            self.sum_right += num

        self.balance_heaps()

    def remove(self, num: int) -> None:
        if num <= -self.left_heap[0]:
            self.left_size -= 1
            self.sum_left -= num
        else:
            self.right_size -= 1
            self.sum_right -= num

        self.lazy_removal[num] += 1
        self.balance_heaps()

    def cost(self) -> int:
        median = -self.left_heap[0]

        return (
            median * self.left_size
            - self.sum_left
            + self.sum_right
            - median * self.right_size
        )


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        N = len(nums)

        cost = [0] * N
        rolling_median = RollingMedian()
        for idx, num in enumerate(nums):
            rolling_median.add(num)

            if idx >= x:
                rolling_median.remove(nums[idx - x])

            if idx >= x - 1:
                cost[idx] = rolling_median.cost()

        dp = [[0] + [inf] * k for _ in range(N)]
        for n_intervals in range(1, k + 1):
            if n_intervals == 1:
                dp[x - 1][n_intervals] = cost[x - 1]
            else:
                dp[n_intervals * x - 1][n_intervals] = (
                    dp[(n_intervals - 1) * x - 1][n_intervals - 1]
                    + cost[n_intervals * x - 1]
                )

        for n_intervals in range(1, k + 1):
            for idx in range(n_intervals * x, N):
                dp[idx][n_intervals] = min(
                    dp[idx - x][n_intervals - 1] + cost[idx], dp[idx - 1][n_intervals]
                )

        return dp[N - 1][k]


sol = Solution()
print(sol.minOperations([5, -2, 1, 3, 7, 3, 6, 4, -1], 3, 2))
print(sol.minOperations([9, -2, -2, -2, 1, 5], 2, 2))
