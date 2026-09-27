class Solution:
    def reverseParentheses(self, s: str) -> str:
        N = len(s)

        def parse(idx: int, first: bool) -> tuple[list[str], int]:
            curr = []
            while idx < N:
                if s[idx] == ")":
                    idx += 1
                    break
                elif s[idx] == "(":
                    word, idx = parse(idx + 1, False)
                    curr += word
                else:
                    curr.append(s[idx])
                    idx += 1
            return (curr[::-1], idx) if not first else (curr, idx)

        ans, _ = parse(0, True)
        return "".join(ans)


sol = Solution()
assert sol.reverseParentheses("(abcd)") == "dcba"
assert sol.reverseParentheses("(u(love)i)") == "iloveu"
assert sol.reverseParentheses("(ed(et(oc))el)") == "leetcode"
