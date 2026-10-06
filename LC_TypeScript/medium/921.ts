import assert from "node:assert";

function minAddToMakeValid(s: string): number {
    let open = 0;
    let adds = 0;

    for (const ch of s) {
        if (ch === "(") open += 1;
        else {
            if (open > 0) open -= 1;
            else adds += 1;
        }
    }

    return open + adds;
}

assert.equal(minAddToMakeValid("())"), 1);
assert.equal(minAddToMakeValid("((("), 3);
