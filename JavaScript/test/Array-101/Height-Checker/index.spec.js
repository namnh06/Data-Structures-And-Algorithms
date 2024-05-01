"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Height_Checker_1 = require("./../../../src/Array-101/Height-Checker");
describe("Height-Checker", function () {
    it("Input: [1] - Output: 0", () => {
        let heights = [1];
        let expected = 0;
        chai_1.assert.deepEqual((0, Height_Checker_1.heightChecker)(heights), expected);
    });
    it("Input: [1, 2] - Output: 0", () => {
        let heights = [1, 2];
        let expected = 0;
        chai_1.assert.deepEqual((0, Height_Checker_1.heightChecker)(heights), expected);
    });
    it("Input: [2, 1] - Output: 2", () => {
        let heights = [2, 1];
        let expected = 2;
        chai_1.assert.deepEqual((0, Height_Checker_1.heightChecker)(heights), expected);
    });
    it("Input: [1, 2 , 3] - Output: 0", () => {
        let heights = [1, 2, 3];
        let expected = 0;
        chai_1.assert.deepEqual((0, Height_Checker_1.heightChecker)(heights), expected);
    });
    it("Input: [2, 1 , 2] - Output: 2", () => {
        let heights = [2, 1, 2];
        let expected = 2;
        chai_1.assert.deepEqual((0, Height_Checker_1.heightChecker)(heights), expected);
    });
    it("Input: [2, 1, 3] - Output: 2", () => {
        let heights = [2, 1, 3];
        let expected = 2;
        chai_1.assert.deepEqual((0, Height_Checker_1.heightChecker)(heights), expected);
    });
    it("Input: [1,1,4,2,1,3] - Output: 3", () => {
        let heights = [1, 1, 4, 2, 1, 3];
        let expected = 3;
        chai_1.assert.deepEqual((0, Height_Checker_1.heightChecker)(heights), expected);
    });
    it("Input: [1,2,3,4,5] - Output: 5", () => {
        let heights = [5, 1, 2, 3, 4];
        let expected = 5;
        chai_1.assert.deepEqual((0, Height_Checker_1.heightChecker)(heights), expected);
    });
    it("Input: [1,2,3,4,5] - Output: 0", () => {
        let heights = [1, 2, 3, 4, 5];
        let expected = 0;
        chai_1.assert.deepEqual((0, Height_Checker_1.heightChecker)(heights), expected);
    });
});
