from math import isqrt


def get_divisors(num: int) -> list[int]:
    divisors = []
    for div in range(1, isqrt(num) + 1):
        if num % div == 0:
            divisors.append(div)
            if num // div != div:
                divisors.append(num // div)
    return divisors


def to_str(nums: list[int]) -> str:
    return ",".join(map(str, nums))


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        ans = 0
        sorted_nums = sorted(nums)
        divisors = get_divisors(len(nums))

        for chunk_len in divisors:
            yep = True
            for left_idx in range(0, len(nums), chunk_len):
                sorted_chunk = to_str(sorted_nums[left_idx : (left_idx + chunk_len)])
                curr_chunk = to_str(nums[left_idx : (left_idx + chunk_len)])

                if sorted_chunk not in (curr_chunk + "," + curr_chunk):
                    yep = False
                    break

            if yep:
                ans += chunk_len

        return ans


sol = Solution()
print(sol.sortableIntegers([3, 1, 2]))
print(sol.sortableIntegers([7, 6, 5]))
print(sol.sortableIntegers([5, 8]))
