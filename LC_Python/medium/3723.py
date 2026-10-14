class Solution:
    def maxSumOfSquares(self, num_digits: int, sum_digits: int) -> str:
        if sum_digits > 9 * num_digits:
            return ""

        ans = "9" * (sum_digits // 9)
        if sum_digits % 9 > 0:
            ans += str(sum_digits % 9)
        ans += "0" * (num_digits - len(ans))

        return ans


sol = Solution()
print(sol.maxSumOfSquares(2, 3))
print(sol.maxSumOfSquares(2, 17))
print(sol.maxSumOfSquares(1, 10))
