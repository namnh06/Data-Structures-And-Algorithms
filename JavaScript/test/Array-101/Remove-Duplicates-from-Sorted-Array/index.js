"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Remove_Duplicates_from_Sorted_Array_1 = require("../../../src/Array-101/Remove-Duplicates-from-Sorted-Array");
describe("Remove-Duplicates-from-Sorted-Array", function () {
    it("Input: [1] - Output: 1", function () {
        let arr = [1];
        let expected = 1;
        chai_1.assert.deepEqual((0, Remove_Duplicates_from_Sorted_Array_1.removeDuplicates)(arr), expected);
    });
    it("Input: [1, 1, 1, 1] - Output: 1", function () {
        let arr = [1, 1, 1, 1];
        let expected = 1;
        chai_1.assert.deepEqual((0, Remove_Duplicates_from_Sorted_Array_1.removeDuplicates)(arr), expected);
    });
    it("Input: [1, 2] - Output: 2", function () {
        let arr = [1, 2];
        let expected = 2;
        chai_1.assert.deepEqual((0, Remove_Duplicates_from_Sorted_Array_1.removeDuplicates)(arr), expected);
    });
    it("Input: [1, 2, 2] - Output: 2", function () {
        let arr = [1, 2, 2];
        let expected = 2;
        chai_1.assert.deepEqual((0, Remove_Duplicates_from_Sorted_Array_1.removeDuplicates)(arr), expected);
    });
    it("Input: [1, 1, 2, 2] - Output: 2", function () {
        let arr = [1, 1, 2, 2];
        let expected = 2;
        chai_1.assert.deepEqual((0, Remove_Duplicates_from_Sorted_Array_1.removeDuplicates)(arr), expected);
    });
    it("Input: [1, 1, 2, 2, 3] - Output: 3", function () {
        let arr = [1, 1, 2, 2, 3];
        let expected = 3;
        chai_1.assert.deepEqual((0, Remove_Duplicates_from_Sorted_Array_1.removeDuplicates)(arr), expected);
    });
    it("Input: [1, 1, 1, 2, 2, 3] - Output: 3", function () {
        let arr = [1, 1, 1, 2, 2, 3];
        let expected = 3;
        chai_1.assert.deepEqual((0, Remove_Duplicates_from_Sorted_Array_1.removeDuplicates)(arr), expected);
    });
});
