import assert from "node:assert";

function digitSum(num: number): number {
    return Array.from(num.toString()).reduce(
        (prev: number, curr: string) => prev + Number.parseInt(curr),
        0
    );
}

function minSwaps(nums: number[]): number {
    const N = nums.length;

    let indices = Array.from({ length: N }, (_, idx) => idx);
    const sums = nums.map(digitSum);
    indices.sort((a, b) => sums[a] - sums[b] || nums[a] - nums[b]);

    const targetPos = Array(N).fill(0);
    for (let pos = 0; pos < N; pos++) {
        targetPos[indices[pos]] = pos;
    }

    const visited = Array(N).fill(false);
    let cycles = 0;

    for (let idx = 0; idx < N; idx++) {
        if (!visited[idx]) {
            cycles++;
            let currIdx = idx;
            while (!visited[currIdx]) {
                visited[currIdx] = true;
                currIdx = targetPos[currIdx];
            }
        }
    }

    return N - cycles;
}

assert.equal(minSwaps([37, 100]), 1);
assert.equal(minSwaps([22, 14, 33, 7]), 0);
assert.equal(minSwaps([18, 43, 34, 16]), 2);
assert.equal(minSwaps([1]), 0);
