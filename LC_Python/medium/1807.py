class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        word_map = dict()
        for w1, w2 in knowledge:
            word_map[w1] = w2

        ans = []
        curr_word = []
        parsing_pair = False
        for letter in s:
            if letter == "(":
                parsing_pair = True
            elif letter == ")":
                word = "".join(curr_word)
                if word in word_map:
                    ans.append(word_map[word])
                else:
                    ans.append("?")
                curr_word = []
                parsing_pair = False
            else:
                if parsing_pair:
                    curr_word.append(letter)
                else:
                    ans.append(letter)
        return "".join(ans)


sol = Solution()
print(sol.evaluate("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]))
print(sol.evaluate("hi(name)", [["a", "b"]]))
print(sol.evaluate("(a)(a)(a)aaa", [["a", "yes"]]))
