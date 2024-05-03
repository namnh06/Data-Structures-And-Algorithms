"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.findDisappearedNumbers = void 0;
function findDisappearedNumbers(nums) {
    let numsLength = nums.length;
    let result = [];
    let numsSorted = quickSort(nums);
    let firstElement = numsSorted[0];
    let lastElement = numsSorted[numsLength - 1];
    if (firstElement > 1) {
        for (let i = 1; i < firstElement; i++) {
            result.push(i);
        }
    }
    if (lastElement < numsLength) {
        for (let i = numsLength; i > lastElement; i--) {
            result.push(i);
        }
    }
    if (numsLength > 2) {
        for (let i = 1; i < numsLength; i++) {
            let diff = numsSorted[i] - numsSorted[i - 1];
            if (diff > 1) {
                for (let j = 1; j < diff; j++) {
                    result.push(numsSorted[i - 1] + j);
                }
            }
        }
    }
    return result;
}
exports.findDisappearedNumbers = findDisappearedNumbers;
function quickSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }
    let pivot = arr[0];
    let left = [];
    let right = [];
    let equals = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] < pivot) {
            left.push(arr[i]);
        }
        else if (arr[i] > pivot) {
            right.push(arr[i]);
        }
        else {
            equals.push(arr[i]);
        }
    }
    return [...quickSort(left), ...equals, ...quickSort(right)];
}
