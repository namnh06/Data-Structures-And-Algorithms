"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const _1480_running_sum_of_1d_array_1 = require("../../src/1480-running-sum-of-1d-array");
describe('Running Sum Of 1D Array', () => {
    it('Input: nums = [1,2,3,4] - Output: [1,3,6,10]', () => {
        const result = _1480_running_sum_of_1d_array_1.runningSum.call(null, [1, 2, 3, 4]);
        chai_1.assert.deepEqual(result, [1, 3, 6, 10]);
    });
    it('Input: nums = [1,1,1,1,1] - Output: [1,2,3,4,5]', () => {
        const result = _1480_running_sum_of_1d_array_1.runningSum.call(null, [1, 1, 1, 1, 1]);
        chai_1.assert.deepEqual(result, [1, 2, 3, 4, 5]);
    });
    it('Input: nums = [3,1,2,10,1] - Output: [3,4,6,16,17]', () => {
        const result = _1480_running_sum_of_1d_array_1.runningSum.call(null, [3, 1, 2, 10, 1]);
        chai_1.assert.deepEqual(result, [3, 4, 6, 16, 17]);
    });
});
