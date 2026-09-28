import assert from "node:assert";

function maxDepth(s: string): number {
    let ans = 0,
        depth = 0;

    for (const letter of s) {
        if (letter === "(") {
            depth += 1;
            ans = Math.max(ans, depth);
        } else if (letter === ")") depth -= 1;
    }

    return ans;
}

assert.equal(maxDepth("(1+(2*3)+((8)/4))+1"), 3);
assert.equal(maxDepth("(1)+((2))+(((3)))"), 3);
assert.equal(maxDepth("()(())((()()))"), 3);
