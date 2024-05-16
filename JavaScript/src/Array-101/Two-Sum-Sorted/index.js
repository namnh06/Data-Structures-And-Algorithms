"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.twoSumSorted = void 0;
function twoSumSorted(nums, target) {
    if (nums.length < 2) {
        return false;
    }
    let left = 0;
    let right = nums.length - 1;
    while (left < right) {
        const total = nums[left] + nums[right];
        if (total < target) {
            left++;
        }
        else if (total > target) {
            right--;
        }
        else {
            return true;
        }
    }
    return false;
}
exports.twoSumSorted = twoSumSorted;
