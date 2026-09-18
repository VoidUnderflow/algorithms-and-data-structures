from collections import defaultdict


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first_and_last = dict()
        for idx, letter in enumerate(s):
            if letter in first_and_last:
                first_and_last[letter][1] = idx
            else:
                first_and_last[letter] = [idx, idx]

        LETTERS = first_and_last.keys()
        eliminates = defaultdict(set)
        intervals = []
        for letter in LETTERS:
            valid = True

            # Expand the interval that contains `letter`.
            left, right = first_and_last[letter]
            idx = left + 1

            while idx <= right:
                curr_letter = s[idx]
                curr_left, curr_right = first_and_last[curr_letter]

                right = max(right, curr_right)
                eliminates[curr_letter].add(letter)

                if curr_left < left:
                    valid = False
                    break

                idx += 1

            if valid:
                intervals.append((letter, left, right))

        # Choose intervals greedily.
        intervals.sort(key=lambda x: x[2] - x[1] + 1)
        eliminated = set()
        ans = []
        for letter, left, right in intervals:
            if letter not in eliminated:
                eliminated = eliminated.union(eliminates[letter])
                ans.append(s[left : (right + 1)])

        return ans


sol = Solution()
print(sol.maxNumOfSubstrings("adefaddaccc"))
print(sol.maxNumOfSubstrings("abbaccd"))
print(sol.maxNumOfSubstrings("dzdabazbbccd"))
