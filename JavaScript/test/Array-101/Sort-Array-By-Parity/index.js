"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Sort_Array_By_Parity_1 = require("../../../src/Array-101/Sort-Array-By-Parity");
describe("Sort-Array-By-Parity", function () {
    it("Input: [0] - Output: [0]", () => {
        let nums = [0];
        let expected = [0];
        chai_1.assert.deepEqual((0, Sort_Array_By_Parity_1.sortArrayByParity)(nums), expected);
    });
    it("Input: [4, 3, 1, 2] - Output: [4, 2, 1, 3]", () => {
        let nums = [4, 3, 1, 2];
        let expected = [4, 2, 1, 3];
        chai_1.assert.deepEqual((0, Sort_Array_By_Parity_1.sortArrayByParity)(nums), expected);
    });
});
