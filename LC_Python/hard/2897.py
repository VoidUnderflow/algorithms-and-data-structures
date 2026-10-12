MODN = 10**9 + 7


class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        bit_count = [0] * 30
        for num in nums:
            bit = 0
            while num > 0:
                if num & 1:
                    bit_count[bit] += 1
                bit += 1
                num >>= 1

        ans = 0
        for _ in range(k):
            curr_num = 0
            for bit_idx, count in enumerate(bit_count):
                if count > 0:
                    curr_num += 1 << bit_idx
                    bit_count[bit_idx] -= 1
            ans += curr_num**2

        return ans % MODN


sol = Solution()
print(sol.maxSum([2, 6, 5, 8], 2))
print(sol.maxSum([4, 5, 4, 7], 3))
