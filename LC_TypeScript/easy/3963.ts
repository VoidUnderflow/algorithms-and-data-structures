function createGrid(m: number, n: number): string[] {
    const ans = Array.from<string>({ length: m }).fill("#".repeat(n - 1) + ".");
    ans[0] = ".".repeat(n);
    return ans;
}

console.log(createGrid(2, 3));
console.log(createGrid(3, 3));
