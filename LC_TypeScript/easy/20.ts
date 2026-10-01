import assert from "node:assert";

const PAIRS = new Map<string, string>([
    [")", "("],
    ["]", "["],
    ["}", "{"],
]);

function isValid(s: string): boolean {
    const stack = [];
    for (const ch of s) {
        if (Array.from(PAIRS.values()).includes(ch)) {
            stack.push(ch);
        } else {
            if (stack.length === 0) return false;
            const topCh = stack.pop()!;
            if (topCh !== PAIRS.get(ch)) return false;
        }
    }
    return stack.length === 0;
}

assert(isValid("()"));
assert(isValid("()[]{}"));
assert(!isValid("(]"));
assert(isValid("([])"));
assert(!isValid("([)]"));
