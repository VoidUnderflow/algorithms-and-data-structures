def get_all_parantheses(
    nr_open: int, nr_closed: int, curr: list[str], n: int
) -> list[str]:
    ans = []
    if nr_open == n:
        return ["".join(curr) + ")" * (n - nr_closed)]

    ans += get_all_parantheses(nr_open + 1, nr_closed, curr + ["("], n)

    if nr_closed < nr_open:
        ans += get_all_parantheses(nr_open, nr_closed + 1, curr + [")"], n)

    return ans


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        return get_all_parantheses(0, 0, [], n)


sol = Solution()
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(1))
