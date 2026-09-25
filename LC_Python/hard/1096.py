class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        ops = []
        sets = []

        def pop_and_op():
            set1 = sets.pop()
            set2 = sets.pop()
            op = ops.pop()

            if op == ",":
                set1 = set1.union(set2)
                sets.append(set1)
            else:
                new_set = set()
                for elem1 in set1:
                    for elem2 in set2:
                        new_set.add(elem2 + elem1)
                sets.append(new_set)

        for idx, char in enumerate(expression):
            match char:
                case "{":
                    if idx > 0 and (
                        expression[idx - 1] == "}" or expression[idx - 1].isalpha()
                    ):
                        ops.append("*")
                    ops.append(char)
                case ",":
                    while len(ops) > 0 and ops[-1] == "*":
                        pop_and_op()
                    ops.append(",")
                case "}":
                    while len(ops) > 0 and ops[-1] != "{":
                        pop_and_op()
                    ops.pop()
                case _:
                    if idx > 0 and (
                        expression[idx - 1] == "}" or expression[idx - 1].isalpha()
                    ):
                        ops.append("*")
                    # A little bit wasteful, but works.
                    sets.append(set(char))

        while len(ops) > 0:
            pop_and_op()

        return sorted(sets[-1])


sol = Solution()
print(sol.braceExpansionII("{a,b}{c,{d,e}}"))
print(sol.braceExpansionII("{{a,z},a{b,c},{ab,z}}"))
