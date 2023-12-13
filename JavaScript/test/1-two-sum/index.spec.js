"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const _1_two_sum_1 = require("../../src/1-two-sum");
describe('Two Sum', () => {
    it('case: nums = [2, 7, 11, 15] - target = 9', () => {
        const result = _1_two_sum_1.twoSum.call(null, [2, 7, 11, 15], 9);
        chai_1.assert.deepEqual(result, [0, 1]);
    });
    it('case: nums = [3, 2, 4] - target = 6', () => {
        const result = _1_two_sum_1.twoSum.call(null, [3, 2, 4], 6);
        chai_1.assert.deepEqual(result, [1, 2]);
    });
    it('case: nums = [3, 3] - target = 6', () => {
        const result = _1_two_sum_1.twoSum.call(null, [3, 3], 6);
        chai_1.assert.deepEqual(result, [0, 1]);
    });
    it('case: nums = [3,2,3]] - target = 6', () => {
        const result = _1_two_sum_1.twoSum.call(null, [3, 2, 3], 6);
        chai_1.assert.deepEqual(result, [0, 2]);
    });
});
