"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.twoSum = void 0;
// https://leetcode.com/problems/two-sum/
function twoSum(nums, target) {
    for (let i = 1; i < nums.length; i++) {
        const total = nums[i - 1] + nums[i];
        if (total == target)
            return [i - 1, i];
        for (let j = 0; j < i; j++) {
            const nextTotal = nums[j] + nums[i];
            if (nextTotal == target)
                return [j, i];
        }
    }
}
exports.twoSum = twoSum;
;
