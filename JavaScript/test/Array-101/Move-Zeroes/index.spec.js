"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Move_Zeroes_1 = require("../../../src/Array-101/Move-Zeroes");
describe("Move-Zeroes", function () {
    it("Input: [0] - Output: [0]", () => {
        let arr = [0];
        let expected = [0];
        chai_1.assert.deepEqual((0, Move_Zeroes_1.moveZeroes)(arr), expected);
    });
    it("Input: [0, 1, 0, 3, 12] - Output: [1, 3, 12, 0, 0]", () => {
        let arr = [0, 1, 0, 3, 12];
        let expected = [1, 3, 12, 0, 0];
        chai_1.assert.deepEqual((0, Move_Zeroes_1.moveZeroes)(arr), expected);
    });
    it("Input: [0, 0, 0] - Output: [0, 0, 0]", () => {
        let arr = [0, 0, 0];
        let expected = [0, 0, 0];
        chai_1.assert.deepEqual((0, Move_Zeroes_1.moveZeroes)(arr), expected);
    });
});
