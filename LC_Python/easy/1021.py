class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        _open = False
        ans = []

        for ch in s:
            if ch == "(":
                if _open:
                    balance += 1
                    ans.append("(")
                else:
                    _open = True
            else:
                if _open:
                    if balance > 0:
                        balance -= 1
                        ans.append(")")
                    else:
                        _open = False
                else:
                    # Should not be reached if well-formed.
                    continue

        return "".join(ans)


sol = Solution()
print(sol.removeOuterParentheses("(()())(())"))
print(sol.removeOuterParentheses("(()())(())(()(()))"))
print(sol.removeOuterParentheses("()()"))
