MODN = 10**9 + 7


class LazySegmentTree:
    def __init__(self, N: int):
        # self.t[tree_idx] = sum of counts in [tL, tR)
        # self.lazy[tree_idx] = pending increment per element
        self.t = [0] * (4 * N)
        self.lazy = [0] * (4 * N)

    # Lazily updates a node (its children are unaffected).
    def apply(self, tree_idx: int, tL: int, tR: int, val: int):
        self.t[tree_idx] += (tR - tL) * val
        self.lazy[tree_idx] += val

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

        self.t[tree_idx] = self.t[2 * tree_idx] + self.t[2 * tree_idx + 1]

    # [tL, tR) and [qL, qR) are guaranteed to overlap
    def query(self, tree_idx: int, tL: int, tR: int, qL: int, qR: int) -> int:
        if qL <= tL and tR <= qR:
            return self.t[tree_idx]

        self.push(tree_idx, tL, tR)
        tM = (tL + tR) // 2

        if qR <= tM:
            return self.query(2 * tree_idx, tL, tM, qL, qR)
        if qL >= tM:
            return self.query(2 * tree_idx + 1, tM, tR, qL, qR)

        return self.query(2 * tree_idx, tL, tM, qL, qR) + self.query(
            2 * tree_idx + 1, tM, tR, qL, qR
        )


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        N = len(nums)
        segment_tree = LazySegmentTree(N)

        last_seen = {}
        curr = 0
        ans = 0

        for idx, num in enumerate(nums):
            last_idx = last_seen.get(num, -1)
            qL, qR = last_idx + 1, idx + 1

            count_sum = segment_tree.query(1, 0, N, qL, qR)
            curr = (curr + 2 * count_sum + (qR - qL)) % MODN

            segment_tree.update(1, 0, N, qL, qR, 1)

            ans = (ans + curr) % MODN
            last_seen[num] = idx

        return ans


sol = Solution()
print(sol.sumCounts([1, 2, 1]))
print(sol.sumCounts([2, 2]))
