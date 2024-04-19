"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Check_If_N_and_Its_Double_Exist_1 = require("./../../../src/Array-101/Check-If-N-and-Its-Double-Exist");
describe('Check-If-N-and-Its-Double-Exist', function () {
    it('Input: [10, 2, 5, 3] - Output: true', function () {
        let arr = [10, 2, 5, 3];
        let expected = true;
        chai_1.assert.deepEqual((0, Check_If_N_and_Its_Double_Exist_1.numberAndDoubleExistInArray)(arr), expected);
    });
    it('Input: [7, 1, 14, 11] - Output: true', function () {
        let arr = [7, 1, 14, 11];
        let expected = true;
        chai_1.assert.deepEqual((0, Check_If_N_and_Its_Double_Exist_1.numberAndDoubleExistInArray)(arr), expected);
    });
    it('Input: [3, 1, 7, 11] - Output: false', function () {
        let arr = [3, 1, 7, 11];
        let expected = false;
        chai_1.assert.deepEqual((0, Check_If_N_and_Its_Double_Exist_1.numberAndDoubleExistInArray)(arr), expected);
    });
    it('Input: [0, 0] - Output: true', function () {
        let arr = [0, 0];
        let expected = true;
        chai_1.assert.deepEqual((0, Check_If_N_and_Its_Double_Exist_1.numberAndDoubleExistInArray)(arr), expected);
    });
    it('Input: [-2,0,10,-19,4,6,-8] - Output: false', function () {
        let arr = [-2, 0, 10, -19, 4, 6, -8];
        let expected = false;
        chai_1.assert.deepEqual((0, Check_If_N_and_Its_Double_Exist_1.numberAndDoubleExistInArray)(arr), expected);
    });
    it('Input: [7,15,3,4,30] - Output: true', function () {
        let arr = [7, 15, 3, 4, 30];
        let expected = true;
        chai_1.assert.deepEqual((0, Check_If_N_and_Its_Double_Exist_1.numberAndDoubleExistInArray)(arr), expected);
    });
});
