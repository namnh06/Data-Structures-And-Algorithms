"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.moveZeroes = void 0;
function moveZeroes(nums) {
    // better in runtime but slower in memory
    let length = nums.length;
    if (length < 2) {
        return nums;
    }
    let markZeroPointer = 0;
    for (let i = 0; i < length; i++) {
        if (nums[i] !== 0) {
            nums[markZeroPointer++] = nums[i];
        }
    }
    while (markZeroPointer < length) {
        nums[markZeroPointer++] = 0;
    }
    return nums;
    // better in memory but slower in runtime
    //     let markZeroPointer: number = -1;
    //     for (let i: number = 0; i < length; i++) {
    //         if (nums[i] === 0) {
    //             if(markZeroPointer === -1) {
    //                 markZeroPointer = i;
    //             }
    //             continue;
    //         }
    //         if (markZeroPointer !== -1) {
    //             let temp: number = nums[i];
    //             nums[i] = nums[markZeroPointer];
    //             nums[markZeroPointer] = temp;
    //             i = markZeroPointer;
    //             markZeroPointer = -1;
    //         }
    //     }
    // for (let i: number = 0; i < length; i++) {
    //     if (nums[i] === 0) {
    //         for (let j: number = i + 1; j < length; j++) {
    //             if (nums[j] !== 0) {
    //                 let temp: number = nums[i];
    //                 nums[i] = nums[j];
    //                 nums[j] = temp;
    //                 break;
    //             }
    //         }
    //     }
    // }
}
exports.moveZeroes = moveZeroes;
