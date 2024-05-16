"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.combineArraysSorted = void 0;
function combineArraysSorted(firstArray, secondArray) {
    const flen = firstArray.length;
    const slen = secondArray.length;
    let result = [];
    if (flen === 0) {
        return secondArray;
    }
    if (slen === 0) {
        return firstArray;
    }
    let pointer = 0;
    while (pointer < flen && pointer < slen) {
        if (firstArray[pointer] <= secondArray[pointer]) {
            result.push(firstArray[pointer]);
            result.push(secondArray[pointer++]);
        }
        else {
            result.push(secondArray[pointer]);
            result.push(firstArray[pointer++]);
        }
    }
    while (pointer < flen) {
        result.push(firstArray[pointer++]);
    }
    while (pointer < slen) {
        result.push(firstArray[pointer++]);
    }
    return result;
}
exports.combineArraysSorted = combineArraysSorted;
