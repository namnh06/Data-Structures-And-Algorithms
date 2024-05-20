"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.combineArraysSorted = void 0;
function combineArraysSorted(firstArray, secondArray) {
    const flen = firstArray.length;
    const slen = secondArray.length;
    let result = [];
    let i = 0;
    let j = 0;
    if (flen === 0) {
        return secondArray;
    }
    if (slen === 0) {
        return firstArray;
    }
    while (i < flen && j < slen) {
        if (firstArray[i] <= secondArray[j]) {
            result.push(firstArray[i++]);
        }
        else {
            result.push(secondArray[j++]);
        }
    }
    while (i < flen) {
        result.push(firstArray[i++]);
    }
    while (j < slen) {
        result.push(secondArray[j++]);
    }
    return result;
}
exports.combineArraysSorted = combineArraysSorted;
