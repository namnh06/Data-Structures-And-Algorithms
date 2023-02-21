"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.runningSum = void 0;
// https://leetcode.com/problems/running-sum-of-1d-array/
function runningSum(nums) {
    let result = [];
    let previousSum = 0;
    nums.forEach(function (num, index) {
        result[index] = previousSum += num;
    });
    return result;
}
exports.runningSum = runningSum;
