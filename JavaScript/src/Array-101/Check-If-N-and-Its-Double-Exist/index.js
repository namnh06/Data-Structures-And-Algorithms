"use strict";
// https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
Object.defineProperty(exports, "__esModule", { value: true });
exports.numberAndDoubleExistInArray = void 0;
function numberAndDoubleExistInArray(arr) {
    if (arr === null || arr.length === 0) {
        return false;
    }
    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = 0; j < arr.length; j++) {
            if (i === j) {
                continue;
            }
            if (arr[i] === arr[j] * 2 || arr[j] === arr[i] * 2) {
                return true;
            }
        }
    }
    return false;
}
exports.numberAndDoubleExistInArray = numberAndDoubleExistInArray;
