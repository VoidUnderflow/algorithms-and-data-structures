class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        N = len(parent)

        children = [[] for _ in range(N)]
        for idx in range(1, N):
            children[parent[idx]].append(idx)

        ans = [1] * N
        prev_node_with_char = dict()

        def dfs(node: int) -> None:
            char = s[node]
            prev_node = prev_node_with_char.get(char, -1)

            prev_node_with_char[char] = node
            for child_node in children[node]:
                dfs(child_node)
            prev_node_with_char[char] = prev_node

            if node == 0:
                return

            if prev_node >= 0:
                ans[prev_node] += ans[node]
            else:
                ans[parent[node]] += ans[node]

        dfs(0)
        return ans


sol = Solution()
print(sol.findSubtreeSizes([-1, 0, 0, 1, 1, 1], "abaabc"))
print(sol.findSubtreeSizes([-1, 0, 4, 0, 1], "abbba"))
