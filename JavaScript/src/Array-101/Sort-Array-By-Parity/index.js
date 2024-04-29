"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.sortArrayByParity = void 0;
function sortArrayByParity(nums) {
    let length = nums.length;
    if (length < 2) {
        return nums;
    }
    let pointer = 0;
    for (let i = 0; i < length; i++) {
        let isEven = nums[i] % 2 === 0;
        if (isEven) {
            let temp = nums[i];
            if (pointer !== i) {
                nums[i] = nums[pointer];
            }
            nums[pointer++] = temp;
        }
    }
    return nums;
}
exports.sortArrayByParity = sortArrayByParity;
