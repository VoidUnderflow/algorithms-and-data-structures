from collections import defaultdict

MODN = 10**9 + 7


class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])

        def within_bounds(x: int, y: int) -> bool:
            return x < M and y < N and x >= 0 and y >= 0

        def get_destination(x: int, y: int, down: bool) -> tuple[int, int]:
            if not within_bounds(x + 1, y + 1):
                return (-1, -1)

            if grid[x + 1][y + 1] == 0:
                return (x + 1, y + 1)

            if down:
                return get_destination(x + 1, y, False)
            else:
                return get_destination(x, y + 1, True)

        inverse_teleport = defaultdict(list)

        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    continue

                if within_bounds(x, y + 1) and grid[x][y + 1] == 1:
                    nx, ny = get_destination(x, y, False)
                    if nx != -1:
                        inverse_teleport[(nx, ny)].append((x, y))

                if within_bounds(x + 1, y) and grid[x + 1][y] == 1:
                    nx, ny = get_destination(x, y, True)
                    if nx != -1:
                        inverse_teleport[(nx, ny)].append((x, y))

        dp = [[0 for _ in range(N)] for _ in range(M)]

        for idx, val in enumerate(grid[0]):
            if val == 1:
                break
            dp[0][idx] = 1

        for x in range(1, M):
            for y in range(N):
                if grid[x][y] == 1:
                    continue

                curr_val = 0

                if grid[x - 1][y] == 0:
                    curr_val += dp[x - 1][y]

                if y > 0 and grid[x][y - 1] == 0:
                    curr_val += dp[x][y - 1]

                for pre_x, pre_y in inverse_teleport[(x, y)]:
                    curr_val += dp[pre_x][pre_y]

                dp[x][y] = curr_val % MODN

        return dp[M - 1][N - 1]


sol = Solution()
print(sol.uniquePaths([[0, 1, 0], [0, 0, 1], [1, 0, 0]]))
print(sol.uniquePaths([[0, 0], [0, 0]]))
print(sol.uniquePaths([[0, 1, 1], [1, 1, 0]]))
print(sol.uniquePaths([[0, 0, 0], [1, 1, 1], [0, 1, 0]]))
