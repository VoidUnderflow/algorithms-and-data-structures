from heapq import heappush, heappop


class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        neighbours = [[] for _ in range(n)]
        for u, v, w in edges:
            neighbours[u].append((v, w))

        # (weight, node, streak)
        heap = [(0, 0, 1)]
        visited = set()

        while len(heap) > 0:
            curr_weight, curr_node, streak = heappop(heap)

            if (curr_node, streak) in visited:
                continue

            if curr_node == n - 1:
                return curr_weight

            visited.add((curr_node, streak))

            for node, weight in neighbours[curr_node]:
                next_streak = streak + 1 if labels[node] == labels[curr_node] else 1

                if next_streak > k:
                    continue

                if (node, next_streak) in visited:
                    continue

                heappush(heap, (curr_weight + weight, node, next_streak))

        return -1


sol = Solution()
print(sol.shortestPath(3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 1))
print(sol.shortestPath(3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], "aab", 2))
print(sol.shortestPath(3, [[0, 1, 1], [1, 2, 1]], "aaa", 2))
