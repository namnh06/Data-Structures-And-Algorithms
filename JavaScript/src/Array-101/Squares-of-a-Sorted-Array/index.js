"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.sortedSquares = void 0;
function sortedSquares(nums) {
    const len = nums.length;
    if (len === 1) {
        return [Math.pow(nums[0], 2)];
    }
    let pointer = len - 1;
    let result = new Array();
    for (let index = 0; index <= pointer; index++) {
        const numIndexSquare = Math.pow(nums[index], 2);
        const numPointerSquare = Math.pow(nums[pointer], 2);
        if (numIndexSquare > numPointerSquare) {
            result.unshift(numIndexSquare);
        }
        else {
            result.unshift(numPointerSquare);
            pointer--;
            index--;
        }
    }
    return result;
}
exports.sortedSquares = sortedSquares;
