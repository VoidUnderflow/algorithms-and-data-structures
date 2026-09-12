from typing import List
from bisect import bisect_left


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)
        events = sorted(
            [
                (left, right, weight, orig_idx)
                for orig_idx, (left, right, weight) in enumerate(intervals)
            ],
            key=lambda event: event[1],
        )

        # best[ii][jj] = (total_weight, sorted tuple) using the first ii
        # events, picking at most jj of them
        best = [[(0, ())] * 5 for _ in range(N + 1)]

        for idx in range(N):
            left_idx, _, weight, orig_idx = events[idx]
            prev_event_idx = bisect_left(
                events, left_idx, hi=idx, key=lambda event: event[1]
            )

            best[idx + 1][0] = best[idx][0]
            for jj in range(1, 5):
                skip = best[idx][jj]

                prev_weight, prev_tuple = best[prev_event_idx][jj - 1]
                take = (prev_weight + weight, tuple(sorted(prev_tuple + (orig_idx,))))

                best[idx + 1][jj] = min(skip, take, key=lambda x: (-x[0], x[1]))

        return list(best[N][4][1])


sol = Solution()
print(
    sol.maximumWeight(
        [[1, 3, 2], [4, 5, 2], [1, 5, 5], [6, 9, 3], [6, 7, 1], [8, 9, 1]]
    )
)
print(
    sol.maximumWeight(
        [[5, 8, 1], [6, 7, 7], [4, 7, 3], [9, 10, 6], [7, 8, 2], [11, 14, 3], [3, 5, 5]]
    )
)
