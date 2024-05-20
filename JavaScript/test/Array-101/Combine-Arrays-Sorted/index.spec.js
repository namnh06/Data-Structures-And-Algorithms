"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Combine_Arrays_Sorted_1 = require("../../../src/Array-101/Combine-Arrays-Sorted");
describe("Combine Arrays Sorted", function () {
    it("Input: [] [1, 2, 3] - Output: [1, 2, 3]", () => {
        const firstArray = [];
        const secondArray = [1, 2, 3];
        const expected = [1, 2, 3];
        chai_1.assert.deepEqual((0, Combine_Arrays_Sorted_1.combineArraysSorted)(firstArray, secondArray), expected);
    });
    it("Input: [1, 2, 2] [] - Output: [1, 2, 2]", () => {
        const firstArray = [1, 2, 2];
        const secondArray = [];
        const expected = [1, 2, 2];
        chai_1.assert.deepEqual((0, Combine_Arrays_Sorted_1.combineArraysSorted)(firstArray, secondArray), expected);
    });
    it("Input: [1] [2] - Output: [1, 2]", () => {
        const firstArray = [1];
        const secondArray = [2];
        const expected = [1, 2];
        chai_1.assert.deepEqual((0, Combine_Arrays_Sorted_1.combineArraysSorted)(firstArray, secondArray), expected);
    });
    it("Input: [1, 2] [2] - Output: [1, 2, 2]", () => {
        const firstArray = [1, 2];
        const secondArray = [2];
        const expected = [1, 2, 2];
        chai_1.assert.deepEqual((0, Combine_Arrays_Sorted_1.combineArraysSorted)(firstArray, secondArray), expected);
    });
    it("Input: [1, 2] [2, 4] - Output: [1, 2, 2, 4]", () => {
        const firstArray = [1, 2];
        const secondArray = [2, 4];
        const expected = [1, 2, 2, 4];
        chai_1.assert.deepEqual((0, Combine_Arrays_Sorted_1.combineArraysSorted)(firstArray, secondArray), expected);
    });
    it("Input: [1, 2] [2, 4, 5] - Output: [1, 2, 2, 4, 5]", () => {
        const firstArray = [1, 2];
        const secondArray = [2, 4, 5];
        const expected = [1, 2, 2, 4, 5];
        chai_1.assert.deepEqual((0, Combine_Arrays_Sorted_1.combineArraysSorted)(firstArray, secondArray), expected);
    });
    it("Input: [1, 2, 6] [2, 4, 5] - Output: [1, 2, 2, 4, 5, 6]", () => {
        const firstArray = [1, 2, 6];
        const secondArray = [2, 4, 5];
        const expected = [1, 2, 2, 4, 5, 6];
        chai_1.assert.deepEqual((0, Combine_Arrays_Sorted_1.combineArraysSorted)(firstArray, secondArray), expected);
    });
});
