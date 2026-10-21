class Solution:
    def minOperations(self, s: str) -> int:
        N = len(s)

        # Check if s is already sorted and calculate the
        # min letter and max letter.
        min_letter, max_letter = s[0], s[0]
        min_count, max_count = 0, 0
        already_sorted = True

        for idx in range(N):
            if idx < N - 1 and s[idx] > s[idx + 1]:
                already_sorted = False

            if s[idx] < min_letter:
                min_count = 1
                min_letter = s[idx]
            elif s[idx] == min_letter:
                min_count += 1

            if s[idx] > max_letter:
                max_letter = s[idx]
                max_count = 1
            elif s[idx] == max_letter:
                max_count += 1

        if already_sorted:
            return 0
        elif N == 2:
            return -1
        elif s[0] == min_letter or s[-1] == max_letter:
            return 1
        elif s[0] == max_letter and s[-1] == min_letter and min_count == max_count == 1:
            return 3
        return 2


sol = Solution()
print(sol.minOperations("dog"))
print(sol.minOperations("card"))
print(sol.minOperations("gf"))
print(sol.minOperations("jgg"))
