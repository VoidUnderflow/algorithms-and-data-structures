class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:
        N_ops = k1 + k2
        diffs = [0]
        N = len(nums1)

        for idx in range(N):
            diffs.append(abs(nums1[idx] - nums2[idx]))
        diffs.sort()

        if N_ops >= sum(diffs):
            return 0

        count = 0
        idx = N
        while idx > 0:
            count += 1
            ops_to_next = (diffs[idx] - diffs[idx - 1]) * count
            if N_ops < ops_to_next:
                break

            N_ops -= ops_to_next
            idx -= 1

        ans = 0
        div, mod = N_ops // count, N_ops % count

        ans += (count - mod) * (diffs[idx] - div) ** 2
        ans += mod * (diffs[idx] - div - 1) ** 2

        idx -= 1
        while idx >= 0:
            ans += diffs[idx] ** 2
            idx -= 1

        return ans


sol = Solution()
print(sol.minSumSquareDiff([1, 2, 3, 4], [2, 10, 20, 19], 0, 0))
print(sol.minSumSquareDiff([1, 4, 10, 12], [5, 8, 6, 9], 1, 1))
print(sol.minSumSquareDiff([11, 12, 13, 14, 15], [13, 16, 16, 12, 14], 3, 6))
