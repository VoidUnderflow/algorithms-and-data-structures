from collections import defaultdict


class Solution:
    def countServers(
        self, n: int, logs: list[list[int]], x: int, queries: list[int]
    ) -> list[int]:
        logs.sort(key=lambda x: x[1])

        Q = len(queries)
        queries = sorted([(queries[idx], idx) for idx in range(Q)])
        ans = [0] * Q

        L = len(logs)
        left_idx, right_idx = 0, 0
        counter = defaultdict(int)
        for query_time, query_idx in queries:
            while right_idx < L and logs[right_idx][1] <= query_time:
                counter[logs[right_idx][0]] += 1
                right_idx += 1

            while left_idx < right_idx and logs[left_idx][1] < query_time - x:
                _id = logs[left_idx][0]
                counter[_id] -= 1
                if counter[_id] == 0:
                    del counter[_id]

                left_idx += 1

            ans[query_idx] = n - len(counter)

        return ans


sol = Solution()
print(sol.countServers(3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11]))
print(sol.countServers(3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4]))
