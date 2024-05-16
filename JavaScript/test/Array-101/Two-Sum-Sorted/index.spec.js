"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Two_Sum_Sorted_1 = require("../../../src/Array-101/Two-Sum-Sorted");
describe("Two Sum Sorted", function () {
    it("Input: [0], 1 - Output: false", () => {
        const nums = [0];
        const target = 4;
        const expected = false;
        chai_1.assert.deepEqual((0, Two_Sum_Sorted_1.twoSumSorted)(nums, target), expected);
    });
    it("Input: [1, 2], 4 - Output: false", () => {
        const nums = [1, 2];
        const target = 4;
        const expected = false;
        chai_1.assert.deepEqual((0, Two_Sum_Sorted_1.twoSumSorted)(nums, target), expected);
    });
    it("Input: [1, 2, 4, 6, 8], 13 - Output: false", () => {
        const nums = [1, 2, 4, 6, 8];
        const target = 13;
        const expected = false;
        chai_1.assert.deepEqual((0, Two_Sum_Sorted_1.twoSumSorted)(nums, target), expected);
    });
    it("Input: [1, 2, 4, 6, 8, 9, 14, 15], 13 - Output: true", () => {
        const nums = [1, 2, 4, 6, 8, 9, 14, 15];
        const target = 13;
        const expected = true;
        chai_1.assert.deepEqual((0, Two_Sum_Sorted_1.twoSumSorted)(nums, target), expected);
    });
});
