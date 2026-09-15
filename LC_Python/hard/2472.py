class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        N = len(s)

        if k == 1:
            return N

        is_palindrome = [[False] * N for _ in range(N)]
        for length in range(1, N):
            for left_idx in range(N - length):
                right_idx = left_idx + length
                if s[left_idx] == s[right_idx] and (
                    length <= 2 or is_palindrome[left_idx + 1][right_idx - 1]
                ):
                    is_palindrome[left_idx][right_idx] = True

        # dp[idx] = how many palindromes of length at least k you can form with s[0..idx-1]
        dp = [0]
        for idx in range(1, N + 1):
            dp.append(dp[-1])
            for left_idx in range(idx - k + 1):
                if is_palindrome[left_idx][idx - 1]:
                    dp[-1] = max(dp[-1], dp[left_idx] + 1)

        return dp[N]


sol = Solution()
print(sol.maxPalindromes("abaccdbbd", 3))
print(sol.maxPalindromes("adbcda", 2))
