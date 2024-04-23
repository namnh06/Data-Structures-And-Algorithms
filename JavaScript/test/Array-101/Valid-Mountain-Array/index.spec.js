"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Valid_Mountain_Array_1 = require("./../../../src/Array-101/Valid-Mountain-Array");
describe("Valid-Mountain-Array", function () {
    it("Input: [2, 1] - Output: false", function () {
        let arr = [2, 1];
        let expected = false;
        chai_1.assert.deepEqual((0, Valid_Mountain_Array_1.validMountainArray)(arr), expected);
    });
    it("Input: [3, 5, 5] - Output: false", function () {
        let arr = [3, 5, 5];
        let expected = false;
        chai_1.assert.deepEqual((0, Valid_Mountain_Array_1.validMountainArray)(arr), expected);
    });
    it("Input: [0,3,2,1] - Output: true", function () {
        let arr = [0, 3, 2, 1];
        let expected = true;
        chai_1.assert.deepEqual((0, Valid_Mountain_Array_1.validMountainArray)(arr), expected);
    });
    it("Input: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - Output: false", function () {
        let arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0];
        let expected = false;
        chai_1.assert.deepEqual((0, Valid_Mountain_Array_1.validMountainArray)(arr), expected);
    });
});
