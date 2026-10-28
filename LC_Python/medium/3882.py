class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        M, N = len(grid), len(grid[0])

        curr_row, prev_row = [set() for _ in range(N)], [set() for _ in range(N)]
        curr_row[0].add(grid[0][0])

        for row in range(M):
            for col in range(N):
                if row == 0 and col == 0:
                    continue

                if col == 0:
                    prev_vals = prev_row[col]
                else:
                    prev_vals = prev_row[col].union(curr_row[col - 1])

                curr_row[col] = {prev_val ^ grid[row][col] for prev_val in prev_vals}

            curr_row, prev_row = prev_row, curr_row

        return min(prev_row[-1])


sol = Solution()
print(sol.minCost([[1, 2], [3, 4]]))
print(sol.minCost([[6, 7], [5, 8]]))
print(sol.minCost([[2, 7, 5]]))
