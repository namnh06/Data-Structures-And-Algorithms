"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Third_Maximum_Number_1 = require("../../../src/Array-101/Third-Maximum-Number");
describe("Third-Maximum-Number", function () {
    it("Input: [1] - Output: 1", () => {
        let nums = [1];
        let expected = 1;
        chai_1.assert.deepEqual((0, Third_Maximum_Number_1.thirdMax)(nums), expected);
    });
    it("Input: [1, 2] - Output: 2", () => {
        let nums = [1, 2];
        let expected = 2;
        chai_1.assert.deepEqual((0, Third_Maximum_Number_1.thirdMax)(nums), expected);
    });
    it("Input: [1, 2, 3] - Output: 1", () => {
        let nums = [1, 2, 3];
        let expected = 1;
        chai_1.assert.deepEqual((0, Third_Maximum_Number_1.thirdMax)(nums), expected);
    });
    it("Input: [1, -1, 3] - Output: -1", () => {
        let nums = [1, -1, 3];
        let expected = -1;
        chai_1.assert.deepEqual((0, Third_Maximum_Number_1.thirdMax)(nums), expected);
    });
    it("Input: [5, 2, 1, 3, 0, 6, 4] - Output: 4", () => {
        let nums = [5, 2, 1, 3, 0, 6, 4];
        let expected = 4;
        chai_1.assert.deepEqual((0, Third_Maximum_Number_1.thirdMax)(nums), expected);
    });
});
