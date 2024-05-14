"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Squares_of_a_Sorted_Array_1 = require("../../../src/Array-101/Squares-of-a-Sorted-Array");
describe("Squares of a Sorted Array", function () {
    it("Input: [0] - Output: [0]", () => {
        let nums = [0];
        let expected = [0];
        chai_1.assert.deepEqual((0, Squares_of_a_Sorted_Array_1.sortedSquares)(nums), expected);
    });
    it("Input: [-2, 1] - Output: [1, 4]", () => {
        let nums = [-2, 1];
        let expected = [1, 4];
        chai_1.assert.deepEqual((0, Squares_of_a_Sorted_Array_1.sortedSquares)(nums), expected);
    });
    it("Input: [-4, -1, 0, 3, 10] - Output: [0, 1, 9, 16, 100]", () => {
        let nums = [-4, -1, 0, 3, 10];
        let expected = [0, 1, 9, 16, 100];
        chai_1.assert.deepEqual((0, Squares_of_a_Sorted_Array_1.sortedSquares)(nums), expected);
    });
});
