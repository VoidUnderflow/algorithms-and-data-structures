DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])

        def in_range(x: int, y: int) -> bool:
            return x >= 0 and x < M and y >= 0 and y < N

        def calc_sum(x: int, y: int) -> int:
            curr_sum = grid[x][y]
            grid[x][y] = 0

            for dx, dy in DELTAS:
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and grid[nx][ny] > 0:
                    curr_sum += calc_sum(nx, ny)

            return curr_sum

        ans = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] > 0:
                    island_sum = calc_sum(x, y)
                    if island_sum % k == 0:
                        ans += 1

        return ans


sol = Solution()
print(
    sol.countIslands(
        [
            [0, 2, 1, 0, 0],
            [0, 5, 0, 0, 5],
            [0, 0, 1, 0, 0],
            [0, 1, 4, 7, 0],
            [0, 2, 0, 0, 8],
        ],
        5,
    )
)
print(sol.countIslands([[3, 0, 3, 0], [0, 3, 0, 3], [3, 0, 3, 0]], 3))
