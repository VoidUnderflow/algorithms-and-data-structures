class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first_and_last = dict()
        for idx, letter in enumerate(s):
            if letter in first_and_last:
                first_and_last[letter][1] = idx
            else:
                first_and_last[letter] = [idx, idx]

        intervals = []
        for letter in first_and_last.keys():
            valid = True

            # Expand the interval that contains `letter`.
            left, right = first_and_last[letter]
            idx = left + 1

            while idx <= right:
                curr_letter = s[idx]
                curr_left, curr_right = first_and_last[curr_letter]

                right = max(right, curr_right)

                if curr_left < left:
                    valid = False
                    break

                idx += 1

            if valid:
                intervals.append((left, right))

        # Choose intervals greedily.
        ans = []
        prev_right = -1
        intervals.sort(key=lambda x: x[1])
        for left, right in intervals:
            if left > prev_right:
                ans.append(s[left : (right + 1)])
                prev_right = right

        return ans


sol = Solution()
print(sol.maxNumOfSubstrings("adefaddaccc"))
print(sol.maxNumOfSubstrings("abbaccd"))
print(sol.maxNumOfSubstrings("dzdabazbbccd"))
