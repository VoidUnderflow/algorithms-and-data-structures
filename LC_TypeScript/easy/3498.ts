import assert from "node:assert";

function reverseDegree(s: string): number {
    return Array.from(s)
        .map((letter, idx) => (122 - letter.charCodeAt(0) + 1) * (idx + 1))
        .reduce((prev: number, curr: number) => prev + curr, 0);
}

assert.equal(reverseDegree("abc"), 148);
assert.equal(reverseDegree("zaza"), 160);
