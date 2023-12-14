// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
export function numberOfSteps(num: number): number {
    let step: number = 0;

    while (num > 0) {
        if (num % 2 !== 0) {
            num--;
        } else {
            num /= 2;
        }
        step++;
    }

    return step;
};
