"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
const chai_1 = require("chai");
const _1342_Number_of_Steps_to_Reduce_a_Number_to_Zero_1 = require("../../src/1342-Number-of-Steps-to-Reduce-a-Number-to-Zero");
describe('1342-Number-of-Steps-to-Reduce-a-Number-to-Zero', () => {
    it('Input: num = 14 - Output: 6', () => {
        const result = _1342_Number_of_Steps_to_Reduce_a_Number_to_Zero_1.numberOfSteps.call(null, 14);
        const expected = 6;
        chai_1.assert.deepEqual(result, expected);
    });
    it('Input: num = 8 - Output: 4', () => {
        const result = _1342_Number_of_Steps_to_Reduce_a_Number_to_Zero_1.numberOfSteps.call(null, 8);
        const expected = 4;
        chai_1.assert.deepEqual(result, expected);
    });
    it('Input: num = 123 - Output: 12', () => {
        const result = _1342_Number_of_Steps_to_Reduce_a_Number_to_Zero_1.numberOfSteps.call(null, 123);
        const expected = 12;
        chai_1.assert.deepEqual(result, expected);
    });
});
