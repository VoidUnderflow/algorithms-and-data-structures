class Solution:
    def minInsertions(self, s: str) -> int:
        s_list = []
        ans = 0

        # Parse s once, '))' -> ')' + fill any missing parantheses.
        idx = 0
        while idx < len(s):
            if s[idx] == "(":
                s_list.append("(")
                idx += 1
            else:
                if idx + 1 < len(s) and s[idx] == s[idx + 1]:
                    s_list.append(")")
                    idx += 2
                else:
                    s_list.append(")")
                    idx += 1
                    ans += 1

        left = 0
        # Parse s_list and add 1 for each missing '('.
        for ch in s_list:
            if ch == "(":
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    ans += 1

        # Add extra '))' for each unmatched '('.
        ans += 2 * left

        return ans


sol = Solution()
print(sol.minInsertions("(()))"))
print(sol.minInsertions("())"))
print(sol.minInsertions("))())("))
