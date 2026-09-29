class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        M, N = len(grid), len(grid[0])

        if (M + N) % 2 == 0:
            return False

        if grid[0][0] == ")" or grid[M - 1][N - 1] == "(":
            return False

        prev_row = [set() for _ in range(N)]
        prev_row[0] = set([0])

        curr_row = [set() for _ in range(N)]

        for row in range(M):
            delta = 1 if grid[row][0] == "(" else -1
            for val in prev_row[0]:
                if val + delta >= 0:
                    curr_row[0].add(val + delta)

            for col in range(1, N):
                delta = 1 if grid[row][col] == "(" else -1
                for val in curr_row[col - 1]:
                    if val + delta >= 0:
                        curr_row[col].add(val + delta)
                for val in prev_row[col]:
                    if val + delta >= 0:
                        curr_row[col].add(val + delta)

            prev_row = curr_row
            curr_row = [set() for _ in range(N)]

        return 0 in prev_row[N - 1]


sol = Solution()
print(
    sol.hasValidPath(
        [["(", "(", "("], [")", "(", ")"], ["(", "(", ")"], ["(", "(", ")"]]
    )
)
print(sol.hasValidPath([[")", ")"], ["(", "("]]))
print(
    sol.hasValidPath(
        [
            ["(", "(", ")", "(", "(", ")", "(", ")", "("],
            [")", "(", "(", "(", ")", ")", ")", "(", "("],
            ["(", ")", ")", "(", "(", ")", "(", "(", "("],
            ["(", "(", ")", "(", ")", "(", "(", ")", "("],
            ["(", ")", "(", ")", ")", ")", "(", ")", ")"],
        ]
    )
)
