"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.replaceElements = void 0;
function replaceElements(arr) {
    // better solution
    let max = arr[arr.length - 1];
    arr[arr.length - 1] = -1;
    for (let i = arr.length - 2; i >= 0; i--) {
        let temp = arr[i];
        arr[i] = max;
        if (temp > max) {
            max = temp;
        }
    }
    return arr;
    //  original solution
    //   if (arr.length === 0) {
    //     return arr;
    //   }
    //   const lastIndex: number = arr.length - 1;
    //   if (arr.length === 1) {
    //     arr[lastIndex] = -1;
    //     return arr;
    //   }
    //   for (let i: number = 0; i < lastIndex; i++) {
    //     let max: number = arr[i + 1];
    //     for (let j: number = i + 1; j < lastIndex; j++) {
    //       if (max < arr[j + 1]) {
    //         max = arr[j + 1];
    //       }
    //     }
    //     arr[i] = max;
    //   }
    //   arr[lastIndex] = -1;
    //   return arr;
}
exports.replaceElements = replaceElements;
