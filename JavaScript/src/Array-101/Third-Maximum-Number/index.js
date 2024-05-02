"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.thirdMax = void 0;
function thirdMax(nums) {
    let arrayLength = nums.length;
    // case [1]
    if (arrayLength === 1) {
        return nums[0];
    }
    // case [1,2]
    if (arrayLength === 2) {
        return nums[0] > nums[1] ? nums[0] : nums[1];
    }
    // case [1,2,3]
    let first = null;
    let second = null;
    let third = null;
    for (let i = 0; i < arrayLength; i++) {
        if (nums[i] === first || nums[i] === second || nums[i] === third) {
            if (nums[i] === first) {
                first = second;
                second = third;
                third = null;
            }
            if (nums[i] === second) {
                second = third;
                third = null;
            }
            if (nums[i] === third) {
                third = null;
            }
        }
        if (first === null) {
            first = nums[i];
            continue;
        }
        else {
            if (nums[i] > first) {
                let temp = first;
                first = nums[i];
                third = second;
                second = temp;
                continue;
            }
        }
        if (second === null) {
            if (nums[i] > first) {
                [first, second] = swap(first, nums[i]);
            }
            else {
                second = nums[i];
            }
            continue;
        }
        else {
            if (nums[i] > second) {
                let temp = second;
                second = nums[i];
                third = temp;
                continue;
            }
        }
        if (third === null) {
            if (nums[i] > first) {
                [first, third] = swap(first, nums[i]);
            }
            else {
                third = nums[i];
            }
        }
        else {
            if (nums[i] > third) {
                third = nums[i];
            }
        }
    }
    return third !== null ? third : first;
}
exports.thirdMax = thirdMax;
function swap(a, b) {
    let temp = a;
    a = b;
    b = temp;
    return [a, b];
}
