from typing import List


def count(digits: List[int]) -> List[int]:
    counts = [0] * 10
    for digit in digits:
        counts[digit] += 1
    return counts


def can_form(base_counts: List[int], curr_counts: List[int]) -> bool:
    for digit in range(10):
        if curr_counts[digit] > base_counts[digit]:
            return False
    return True


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        base_counts = count(digits)
        ans = 0

        for num in range(100, 1000, 2):
            if can_form(base_counts, count([int(x) for x in str(num)])):
                ans += 1

        return ans


sol = Solution()
print(sol.totalNumbers([1, 2, 3, 4]))
print(sol.totalNumbers([0, 2, 2]))
print(sol.totalNumbers([6, 6, 6]))
print(sol.totalNumbers([1, 3, 5]))
