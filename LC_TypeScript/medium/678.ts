import assert from "node:assert";

function checkValidString(s: string): boolean {
    let open: number[] = [],
        star: number[] = [];

    for (let idx = 0; idx < s.length; idx++) {
        const ch = s[idx];
        if (ch === "(") open.push(idx);
        else if (ch === "*") star.push(idx);
        else {
            if (open.length > 0) open.pop();
            else if (star.length > 0) star.pop();
            else return false;
        }
    }

    while (open.length > 0) {
        if (star.length > 0 && star.at(-1)! > open.at(-1)!) {
            star.pop();
            open.pop();
        } else return false;
    }

    return true;
}

assert(checkValidString("()"));
assert(checkValidString("(*)"));
assert(checkValidString("(*))"));
assert(!checkValidString("("));
assert(!checkValidString("(((((()*)(*)*))())())(()())())))((**)))))(()())()"));
