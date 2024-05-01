"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.heightChecker = void 0;
function heightChecker(heights) {
    let arrayLength = heights.length;
    if (arrayLength <= 1) {
        return 0;
    }
    // sorting array non-decreasing
    let heightsSorted = quickSort(heights);
    let indices = 0;
    // count indices
    for (let index = 0; index < arrayLength; index++) {
        if (heightsSorted[index] !== heights[index]) {
            indices++;
        }
    }
    return indices;
}
exports.heightChecker = heightChecker;
function quickSort(arr) {
    if (arr.length < 2) {
        return arr;
    }
    let pivot = arr[0];
    let left = []; // Initialize the 'left' array
    let right = []; // Initialize the 'right' array
    let equals = []; // Array to hold elements equal to pivot
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
