"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.removeElement = void 0;
function removeElement(nums, val) {
    // smarter solution
    let index = 0;
    let length = nums.length;
    while (index < length) {
        if (nums[index] === val) {
            nums[index] = nums[--length];
        }
        else {
            index++;
        }
    }
    return length;
    // original
    //   let k: number = 0;
    //   let lengthNums: number = nums.length;
    //   if (lengthNums <= 1) {
    //     if (lengthNums === 1 && nums[0] !== val) {
    //       return 1;
    //     }
    //     return k;
    //   }
    //   for (let i: number = 0; i < lengthNums; i++) {
    //     if (nums[i] !== val) {
    //       nums[k] = nums[i];
    //       if (i !== k++) {
    //         nums[i] = val;
    //       }
    //     }
    //   }
    //   return k;
}
exports.removeElement = removeElement;
