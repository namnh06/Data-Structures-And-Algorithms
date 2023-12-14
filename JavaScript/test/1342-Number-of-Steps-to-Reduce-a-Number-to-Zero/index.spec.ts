// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
import { assert } from 'chai';
import { numberOfSteps } from '../../src/1342-Number-of-Steps-to-Reduce-a-Number-to-Zero';

describe('1342-Number-of-Steps-to-Reduce-a-Number-to-Zero', () => {
    it('Input: num = 14 - Output: 6', () => {
        const result = numberOfSteps.call(null, 14);
        const expected = 6;
        assert.deepEqual(result, expected);
    });

    it('Input: num = 8 - Output: 4', () => {
        const result = numberOfSteps.call(null, 8);
        const expected = 4;
        assert.deepEqual(result, expected);
    });

    it('Input: num = 123 - Output: 12', () => {
        const result = numberOfSteps.call(null, 123);
        const expected = 12;
        assert.deepEqual(result, expected);
    });
})
