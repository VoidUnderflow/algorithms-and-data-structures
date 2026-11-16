class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s

        curr_str = []
        for idx in range(0, len(s), k):
            curr_str.append(str(sum([int(digit) for digit in s[idx : (idx + k)]])))
        return self.digitSum("".join(curr_str), k)


sol = Solution()
print(sol.digitSum("11111222223", 3))
print(sol.digitSum("00000000", 3))
