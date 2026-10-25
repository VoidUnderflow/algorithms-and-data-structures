class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])
        ans = 0

        def fill_island(ii, jj):
            if ii < 0 or jj < 0 or ii >= M or jj >= N or grid[ii][jj] == 1:
                return

            grid[ii][jj] = 1

            fill_island(ii + 1, jj)
            fill_island(ii - 1, jj)
            fill_island(ii, jj + 1)
            fill_island(ii, jj - 1)

        # Set connected components touching the edges to 1.
        for ii in range(M):
            for jj in [0, N - 1]:
                if grid[ii][jj] == 0:
                    fill_island(ii, jj)

        for jj in range(N):
            for ii in [0, M - 1]:
                if grid[ii][jj] == 0:
                    fill_island(ii, jj)

        # Count closed islands.
        for ii in range(1, M - 1):
            for jj in range(1, N - 1):
                if grid[ii][jj] == 0:
                    ans += 1
                    fill_island(ii, jj)

        return ans


sol = Solution()
print(
    sol.closedIsland(
        [
            [1, 1, 1, 1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ]
    )
)
print(sol.closedIsland([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]))
print(
    sol.closedIsland(
        [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]
    )
)
