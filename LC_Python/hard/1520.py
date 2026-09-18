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
            # Expand the interval that contains `letter`.
            min_left, max_right = first_and_last[letter]
            indices = list(range(min_left, max_right + 1))
            while len(indices) > 0:
                idx = indices.pop()
                left, right = first_and_last[s[idx]]

                if left < min_left:
                    indices += list(range(left, min_left))
                    min_left = left

                if right > max_right:
                    indices += list(range(max_right + 1, right + 1))
                    max_right = right

                # Selecting s[idx] => can't choose letter anymore.
                eliminates[s[idx]].add(letter)

            intervals.append((letter, min_left, max_right))

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
