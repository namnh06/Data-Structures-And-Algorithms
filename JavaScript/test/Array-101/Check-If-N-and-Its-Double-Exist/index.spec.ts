import { assert } from 'chai';

import { numberAndDoubleExistInArray } from './../../../src/Array-101/Check-If-N-and-Its-Double-Exist';

describe('Check-If-N-and-Its-Double-Exist', function () {
    it('Input: [10, 2, 5, 3] - Output: true', function () {
        let arr: number[] = [10, 2, 5, 3];
        let expected: boolean = true;
        assert.deepEqual(numberAndDoubleExistInArray(arr), expected);
    });

    it('Input: [7, 1, 14, 11] - Output: true', function () {
        let arr: number[] = [7, 1, 14, 11];
        let expected: boolean = true;
        assert.deepEqual(numberAndDoubleExistInArray(arr), expected);
    });

    it('Input: [3, 1, 7, 11] - Output: false', function () {
        let arr: number[] = [3, 1, 7, 11];
        let expected: boolean = false;
        assert.deepEqual(numberAndDoubleExistInArray(arr), expected);
    });

    it('Input: [0, 0] - Output: true', function () {
        let arr: number[] = [0, 0];
        let expected: boolean = true;
        assert.deepEqual(numberAndDoubleExistInArray(arr), expected);
    });

    it('Input: [-2,0,10,-19,4,6,-8] - Output: false', function () {
        let arr: number[] = [-2,0,10,-19,4,6,-8];
        let expected: boolean = false;
        assert.deepEqual(numberAndDoubleExistInArray(arr), expected);
    });

    it('Input: [7,15,3,4,30] - Output: true', function () {
        let arr: number[] = [7,15,3,4,30];
        let expected: boolean = true;
        assert.deepEqual(numberAndDoubleExistInArray(arr), expected);
    });
});