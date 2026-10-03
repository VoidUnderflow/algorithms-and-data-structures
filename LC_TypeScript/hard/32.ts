import assert from "node:assert";

function longestValidParentheses(s: string): number {
    let ans = 0;
    const stack = [-1];

    Array.from(s).map((char, idx) => {
        if (char === "(") {
            stack.push(idx);
        } else {
            stack.pop();
            if (stack.length === 0) stack.push(idx);
            else ans = Math.max(ans, idx - stack.at(-1)!);
        }
    });

    return ans;
}

assert.equal(longestValidParentheses("(()"), 2);
assert.equal(longestValidParentheses(")()())"), 4);
assert.equal(longestValidParentheses(""), 0);
