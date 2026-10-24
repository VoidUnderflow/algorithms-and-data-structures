import assert from "node:assert";

function toTime(strDate: string): number {
    return new Date("2026-" + strDate).getTime();
}

function toDays(timeDiff: number): number {
    return Math.round(timeDiff / (1000 * 60 * 60 * 24));
}

function countDaysTogether(
    arriveAlice: string,
    leaveAlice: string,
    arriveBob: string,
    leaveBob: string
): number {
    const [arrA, leaveA] = [toTime(arriveAlice), toTime(leaveAlice)];
    const [arrB, leaveB] = [toTime(arriveBob), toTime(leaveBob)];

    const intervalStart = Math.max(arrA, arrB);
    const intervalEnd = Math.min(leaveA, leaveB);

    if (intervalStart > intervalEnd) return 0;
    return toDays(intervalEnd - intervalStart) + 1;
}

assert.equal(countDaysTogether("08-15", "08-18", "08-16", "08-19"), 3);
assert.equal(countDaysTogether("10-01", "10-31", "11-01", "12-31"), 0);
