"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.twoSum = void 0;
// https://leetcode.com/problems/two-sum/
function twoSum(nums, target) {
    const numsLength = nums.length;
    if (numsLength < 2 || numsLength > Math.pow(10, 4)) {
        return;
    }
    for (let i = 0; i < numsLength; i++) {
        if (i == 0) {
            continue;
        }
        const total = nums[i - 1] + nums[i];
        if (total == target) {
            return [i - 1, i];
        }
    }
}
exports.twoSum = twoSum;
;
