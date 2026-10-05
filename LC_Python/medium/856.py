class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for idx, ch in enumerate(s):
            if ch == "(":
                stack.append((idx, 0))
            else:
                if stack[-1][1] == 0:
                    stack.pop()
                    stack.append((-1, 1))
                else:
                    curr_val = 0
                    while stack[-1][1] != 0:
                        _, val = stack.pop()
                        curr_val += val
                    stack.pop()
                    stack.append((-1, 2 * curr_val))

        ans = 0
        while stack:
            _, val = stack.pop()
            ans += val

        return ans


sol = Solution()
print(sol.scoreOfParentheses("()"))
print(sol.scoreOfParentheses("(())"))
print(sol.scoreOfParentheses("()()"))
print(sol.scoreOfParentheses("((()))()"))
print(sol.scoreOfParentheses("(()(()))"))
