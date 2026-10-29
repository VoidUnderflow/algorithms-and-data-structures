from dataclasses import dataclass


@dataclass(slots=True)
class TreeNode:
    mask: int = 0
    parent_idx: int = -1
    depth: int = 0
    entry_idx: int = 0
    exit_idx: int = 0
    size: int = 1


class LazySegmentTree:
    def __init__(self, nums: list[int]):
        N = len(nums)

        # self.t[tree_idx] = XOR of values in [tL, tR)
        # self.lazy[tree_idx] = pending XOR per element
        self.t = [0] * (4 * N)
        self.lazy = [0] * (4 * N)
        self.build(1, 0, N, nums)

    def build(self, tree_idx: int, tL: int, tR: int, nums: list[int]):
        if tR - tL == 1:
            self.t[tree_idx] = nums[tL]
            return

        tM = (tL + tR) // 2
        self.build(2 * tree_idx, tL, tM, nums)
        self.build(2 * tree_idx + 1, tM, tR, nums)
        self.t[tree_idx] = self.t[2 * tree_idx] ^ self.t[2 * tree_idx + 1]

    # Lazily updates a node (its children are unaffected).
    def apply(self, tree_idx: int, tL: int, tR: int, val: int):
        if (tR - tL) % 2:
            self.t[tree_idx] ^= val
        self.lazy[tree_idx] ^= val

    # Push lazy updates through to children.
    def push(self, tree_idx: int, tL: int, tR: int):
        val = self.lazy[tree_idx]
        if val == 0:
            return

        tM = (tL + tR) // 2
        self.apply(2 * tree_idx, tL, tM, val)
        self.apply(2 * tree_idx + 1, tM, tR, val)
        self.lazy[tree_idx] = 0

    # Update range; [tL, tR) and [qL, qR) are guaranteed to overlap.
    def update(self, tree_idx: int, tL: int, tR: int, qL: int, qR: int, val: int):
        if qL <= tL and tR <= qR:
            self.apply(tree_idx, tL, tR, val)
            return

        self.push(tree_idx, tL, tR)
        tM = (tL + tR) // 2

        if qL < tM:
            self.update(2 * tree_idx, tL, tM, qL, qR, val)
        if qR > tM:
            self.update(2 * tree_idx + 1, tM, tR, qL, qR, val)

        self.t[tree_idx] = self.t[2 * tree_idx] ^ self.t[2 * tree_idx + 1]

    # [tL, tR) and [qL, qR) are guaranteed to overlap.
    def query(self, tree_idx: int, tL: int, tR: int, qL: int, qR: int) -> int:
        if qL <= tL and tR <= qR:
            return self.t[tree_idx]

        self.push(tree_idx, tL, tR)
        tM = (tL + tR) // 2

        if qR <= tM:
            return self.query(2 * tree_idx, tL, tM, qL, qR)
        if qL >= tM:
            return self.query(2 * tree_idx + 1, tM, tR, qL, qR)

        return self.query(2 * tree_idx, tL, tM, qL, qR) ^ self.query(
            2 * tree_idx + 1, tM, tR, qL, qR
        )


class Solution:
    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        nodes = [TreeNode(mask=1 << (ord(c) - ord("a"))) for c in s]

        neighbours = [[] for _ in range(n)]
        for n1_idx, n2_idx in edges:
            neighbours[n1_idx].append(n2_idx)
            neighbours[n2_idx].append(n1_idx)

        # DFS flattening and initial prefix XORs.
        order = []  # order[x] = y => node y (0..n-1) was the xth node visited in the DFS
        initial_prefixes = [0] * n
        stack = [0]
        initial_prefixes[0] = nodes[0].mask

        # A node's subtree is represented by [node.entry_idx, node.exit_idx).
        # entry_idx, exit_idx are indices of order
        while stack:
            n1_idx = stack.pop()
            n1 = nodes[n1_idx]

            n1.entry_idx = len(order)
            order.append(n1_idx)

            for n2_idx in neighbours[n1_idx]:
                if n2_idx == n1.parent_idx:
                    continue

                n2 = nodes[n2_idx]
                n2.parent_idx = n1_idx
                n2.depth = n1.depth + 1
                initial_prefixes[n2_idx] = initial_prefixes[n1_idx] ^ n2.mask
                stack.append(n2_idx)

        # Calculate node size.
        for n1_idx in reversed(order[1:]):
            n1 = nodes[n1_idx]
            nodes[n1.parent_idx].size += n1.size

        # Calculate exit_idx for each node based on size.
        for n1 in nodes:
            n1.exit_idx = n1.entry_idx + n1.size

        # O(N) LCA, pray to god we don't need something more efficient.
        def lca(u_idx: int, v_idx: int) -> int:
            while nodes[u_idx].depth > nodes[v_idx].depth:
                u_idx = nodes[u_idx].parent_idx
            while nodes[v_idx].depth > nodes[u_idx].depth:
                v_idx = nodes[v_idx].parent_idx

            while u_idx != v_idx:
                u_idx = nodes[u_idx].parent_idx
                v_idx = nodes[v_idx].parent_idx

            return u_idx

        # We use a lazy segment tree to do efficient range updates.
        # The tree stores the xor prefix for each node.
        # Updating the value of a TreeNode -> map [entry_idx, exit_idx) -> lazy range update in the segment tree using a xor trick
        # (old = prefix ^ old_mask, delta = old_mask ^ new mask, new = old ^ delta = prefix ^ new_mask; true, since x ^ x = 0, 0 ^ x = x)
        segment_tree = LazySegmentTree(
            [initial_prefixes[node_idx] for node_idx in order]
        )

        ans = []
        for q in queries:
            op, arg1, arg2 = q.split()
            n1_idx = int(arg1)
            n1 = nodes[n1_idx]

            if op == "update":
                new_mask = 1 << (ord(arg2) - ord("a"))
                delta = n1.mask ^ new_mask
                segment_tree.update(1, 0, n, n1.entry_idx, n1.exit_idx, delta)
                n1.mask = new_mask
            else:
                n2_idx = int(arg2)
                n2 = nodes[n2_idx]
                lca_node_idx = lca(n1_idx, n2_idx)

                n1_prefix = segment_tree.query(1, 0, n, n1.entry_idx, n1.entry_idx + 1)
                n2_prefix = segment_tree.query(1, 0, n, n2.entry_idx, n2.entry_idx + 1)

                path_mask = n1_prefix ^ n2_prefix ^ nodes[lca_node_idx].mask
                ans.append(path_mask.bit_count() <= 1)

        return ans


sol = Solution()
print(
    sol.palindromePath(
        3, [[0, 1], [1, 2]], "aac", ["query 0 2", "update 1 b", "query 0 2"]
    )
)
print(
    sol.palindromePath(
        4,
        [[0, 1], [0, 2], [0, 3]],
        "abca",
        ["query 1 2", "update 0 b", "query 2 3", "update 3 a", "query 1 3"],
    )
)
