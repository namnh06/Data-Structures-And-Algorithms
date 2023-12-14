"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.numberOfSteps = void 0;
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
function numberOfSteps(num) {
    let step = 0;
    while (num > 0) {
        if (num % 2 !== 0) {
            num--;
        }
        else {
            num /= 2;
        }
        step++;
    }
    return step;
}
exports.numberOfSteps = numberOfSteps;
;
