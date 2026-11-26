class Solution:
    def canAliceWin(self, n: int) -> bool:
        n_steps = 0
        chunk = 10

        while n >= chunk:
            n -= chunk
            chunk -= 1
            n_steps += 1

        return n_steps % 2 == 1


sol = Solution()
print(sol.canAliceWin(12))
print(sol.canAliceWin(1))
