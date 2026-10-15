from collections import Counter


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        counters = []
        curr_counter = Counter()
        for num in nums:
            curr_counter = curr_counter.copy()
            curr_counter[num] += 1
            counters.append(curr_counter)

        N = len(nums)
        ans = 0
        for ii in range(N):
            for jj in range(ii, N):
                if ii > 0:
                    ans += len(counters[jj] - counters[ii - 1]) ** 2
                else:
                    ans += len(counters[jj]) ** 2

        return ans


sol = Solution()
print(sol.sumCounts([1, 2, 1]))
print(sol.sumCounts([1, 1]))
