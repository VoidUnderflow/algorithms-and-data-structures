# TODO: Merge should probably modify in-place.
class YetAnotherSegmentTree:
    def __init__(self, nums: list[int], k: int):
        N = len(nums)

        # tree_idx -> [tL, tR]
        # self.t[tree_idx][k] = nums[tL] * ... * nums[tR] (mod k)
        # self.t[tree_idx][x], x in [0, k-1] number of subarrays starting at tL s.t. the product
        # of their elements are x mod k
        self.t = [[0] * (k + 1) for _ in range(4 * N)]
        self.k = k
        self.build(nums, 1, 0, N)

    def build(self, nums: list[int], tree_idx: int, tL: int, tR: int):
        if tL + 1 == tR:
            self.reset_leaf(tree_idx, nums[tL])
        else:
            tM = (tL + tR) // 2
            self.build(nums, 2 * tree_idx, tL, tM)
            self.build(nums, 2 * tree_idx + 1, tM, tR)
            self.t[tree_idx] = self.merge_segments(
                self.t[2 * tree_idx], self.t[2 * tree_idx + 1]
            )

    def reset_leaf(self, tree_idx: int, val: int):
        self.t[tree_idx] = [0] * (self.k + 1)
        self.t[tree_idx][val % self.k] = 1
        self.t[tree_idx][self.k] = val % self.k

    def merge_segments(self, seg1: list[int], seg2: list[int]) -> list[int]:
        merge_res = [0] * (self.k + 1)
        merge_res[-1] = (seg1[-1] * seg2[-1]) % self.k

        for mod in range(self.k):
            merge_res[mod] = seg1[mod]

        for mod in range(self.k):
            merge_res[(seg1[-1] * mod) % self.k] += seg2[mod]

        return merge_res

    def update(self, tree_idx: int, tL: int, tR: int, orig_idx: int, new_val: int):
        if tL + 1 == tR:
            self.reset_leaf(tree_idx, new_val)
        else:
            tM = (tL + tR) // 2
            if orig_idx < tM:
                self.update(2 * tree_idx, tL, tM, orig_idx, new_val)
            else:
                self.update(2 * tree_idx + 1, tM, tR, orig_idx, new_val)
            self.t[tree_idx] = self.merge_segments(
                self.t[2 * tree_idx], self.t[2 * tree_idx + 1]
            )

    # [tL, tR) and [qL, qR) are guaranteed to have an overlap
    def query(self, tree_idx: int, tL: int, tR: int, qL: int, qR: int):
        # Query includes the current segment.
        if qL <= tL and tR <= qR:
            return self.t[tree_idx]

        tM = (tL + tR) // 2
        if qR <= tM:
            return self.query(2 * tree_idx, tL, tM, qL, qR)
        if qL >= tM:
            return self.query(2 * tree_idx + 1, tM, tR, qL, qR)

        left_segment = self.query(2 * tree_idx, tL, tM, qL, qR)
        right_segment = self.query(2 * tree_idx + 1, tM, tR, qL, qR)
        return self.merge_segments(left_segment, right_segment)


class Solution:
    def resultArray(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[int]:
        N = len(nums)
        segment_tree = YetAnotherSegmentTree(nums, k)
        ans = []

        for idx, val, start, x in queries:
            segment_tree.update(1, 0, N, idx, val)
            segment = segment_tree.query(1, 0, N, start, N)
            ans.append(segment[x])

        return ans


sol = Solution()
print(sol.resultArray([1, 2, 3, 4, 5], 3, [[2, 2, 0, 2], [3, 3, 3, 0], [0, 1, 0, 1]]))
print(sol.resultArray([1, 2, 4, 8, 16, 32], 4, [[0, 2, 0, 2], [0, 2, 0, 1]]))
print(sol.resultArray([1, 1, 2, 1, 1], 2, [[2, 1, 0, 1]]))
