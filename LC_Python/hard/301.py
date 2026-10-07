class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left, right = 0, 0

        for ch in s:
            if ch == "(":
                left += 1
            elif ch == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1

        ans = set()
        N = len(s)

        def backtrack(
            idx: int,
            curr: list[str],
            rem_left: int,
            rem_right: int,
            curr_left: int,
            curr_right: int,
        ):
            if idx == N:
                if rem_left == left and rem_right == right and curr_left == curr_right:
                    ans.add("".join(curr))
                return

            if s[idx] == "(":
                # Keep
                backtrack(
                    idx + 1,
                    curr + ["("],
                    rem_left,
                    rem_right,
                    curr_left + 1,
                    curr_right,
                )
                # Remove
                if rem_left < left:
                    backtrack(
                        idx + 1, curr, rem_left + 1, rem_right, curr_left, curr_right
                    )
            elif s[idx] == ")":
                # Is it still valid if we keep?
                if curr_left > curr_right:
                    backtrack(
                        idx + 1,
                        curr + [")"],
                        rem_left,
                        rem_right,
                        curr_left,
                        curr_right + 1,
                    )
                # Remove
                if rem_right < right:
                    backtrack(
                        idx + 1, curr, rem_left, rem_right + 1, curr_left, curr_right
                    )
            else:
                backtrack(
                    idx + 1, curr + [s[idx]], rem_left, rem_right, curr_left, curr_right
                )

        backtrack(0, [], 0, 0, 0, 0)
        return list(ans)


sol = Solution()
print(sol.removeInvalidParentheses("()())()"))
print(sol.removeInvalidParentheses("(a)())()"))
