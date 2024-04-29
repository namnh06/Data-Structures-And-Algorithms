"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Remove_Element_1 = require("../../../src/Array-101/Remove-Element");
describe("Remove-Elements", function () {
    it("Input: [] - Val Remove: 1 - Output: 0", () => {
        let nums = [];
        let valRemove = 1;
        let expected = 0;
        chai_1.assert.deepEqual((0, Remove_Element_1.removeElement)(nums, valRemove), expected);
    });
    it("Input: [0] - Val Remove: 1 - Output: 1", () => {
        let nums = [0];
        let valRemove = 1;
        let expected = 1;
        chai_1.assert.deepEqual((0, Remove_Element_1.removeElement)(nums, valRemove), expected);
    });
    it("Input: [1] - Val Remove: 1 - Output: 0", () => {
        let nums = [1];
        let valRemove = 1;
        let expected = 0;
        chai_1.assert.deepEqual((0, Remove_Element_1.removeElement)(nums, valRemove), expected);
    });
    it("Input: [1, 1] - Val Remove: 1 - Output: 0", () => {
        let nums = [1, 1];
        let valRemove = 1;
        let expected = 0;
        chai_1.assert.deepEqual((0, Remove_Element_1.removeElement)(nums, valRemove), expected);
    });
    it("Input: [0,1,2,2,3,0,4,2] - Val Remove: 2 - Output: 5", () => {
        let nums = [0, 1, 2, 2, 3, 0, 4, 2];
        let valRemove = 2;
        let expected = 5;
        chai_1.assert.deepEqual((0, Remove_Element_1.removeElement)(nums, valRemove), expected);
    });
    2;
});
