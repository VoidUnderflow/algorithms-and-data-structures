class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        ans = []

        for char in seq:
            if char == "(":
                depth += 1
                ans.append(0 if depth % 2 == 1 else 1)
            else:
                depth -= 1
                ans.append(0 if depth % 2 == 0 else 1)

        return ans


sol = Solution()
print(sol.maxDepthAfterSplit("(()())"))
print(sol.maxDepthAfterSplit("()(())()"))
