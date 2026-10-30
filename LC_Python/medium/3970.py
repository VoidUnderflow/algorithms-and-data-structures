from heapq import heappush, heappop


class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        neighbours = [[] for _ in range(n)]
        for u, v, w in edges:
            neighbours[u].append((v, w))

        # (weight, (node, last_char, last_char_streak))
        heap = [(0, (0, "", 0))]

        visited = [False] * n
        visited[0] = True

        while len(heap) > 0:
            curr_weight, (curr_node, last_char, last_char_streak) = heappop(heap)
            if labels[curr_node] != last_char:
                last_char_streak = 1
            elif last_char_streak == k:
                continue  # reached streak limit
            else:
                last_char_streak += 1

            if curr_node == n - 1:
                return curr_weight

            visited[curr_node] = True

            for node, weight in neighbours[curr_node]:
                if visited[node]:
                    continue

                heappush(
                    heap,
                    (curr_weight + weight, (node, labels[curr_node], last_char_streak)),
                )

        return -1


sol = Solution()
print(sol.shortestPath(3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 1))
print(sol.shortestPath(3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 2))
print(sol.shortestPath(3, [[0, 1, 1], [1, 2, 1]], "aaa", 2))
