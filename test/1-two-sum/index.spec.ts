import { assert } from 'chai';
import { twoSum } from '../../src/1-two-sum';

describe('Two Sum', () => {
    it('case: nums = [2, 7, 11, 15] - target = 9', () => {
        const result = twoSum.call(null, [2, 7, 11, 15], 9);
        assert.deepEqual(result, [0, 1]);
    });

    it('case: nums = [3, 2, 4] - target = 6', () => {
        const result = twoSum.call(null, [3, 2, 4], 6);
        assert.deepEqual(result, [1, 2]);
    });

    it('case: nums = [3, 3] - target = 6', () => {
        const result = twoSum.call(null, [3, 3], 6);
        assert.deepEqual(result, [0, 1]);
    });
});