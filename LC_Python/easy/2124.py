class Solution:
    def checkString(self, s: str) -> bool:
        found_b = False

        for char in s:
            if char == "a":
                if found_b:
                    return False
            else:
                found_b = True

        return True


sol = Solution()
print(sol.checkString("aaabbb"))
print(sol.checkString("abab"))
print(sol.checkString("bbb"))
