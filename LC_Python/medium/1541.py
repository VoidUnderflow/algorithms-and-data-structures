class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        idx, left = 0, 0

        while idx < len(s):
            if s[idx] == "(":
                left += 1
                idx += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    ans += 1

                if idx + 1 < len(s) and s[idx] == s[idx + 1]:
                    idx += 2
                else:
                    ans += 1
                    idx += 1

        ans += left * 2
        return ans


sol = Solution()
print(sol.minInsertions("(()))"))
print(sol.minInsertions("())"))
print(sol.minInsertions("))())("))
