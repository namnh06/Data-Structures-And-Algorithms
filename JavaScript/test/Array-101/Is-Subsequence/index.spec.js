"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Is_Subsequence_1 = require("../../../src/Array-101/Is-Subsequence");
describe("Is Subsequence", function () {
    it("Input: 'abc' 'ahbgdc' - Output: true", () => {
        const s = "abc";
        const t = "ahbgdc";
        const expected = true;
        chai_1.assert.deepEqual((0, Is_Subsequence_1.isSubsequence)(s, t), expected);
    });
    it("Input: 'axc' 'ahbgdc' - Output: false", () => {
        const s = "axc";
        const t = "ahbgdc";
        const expected = false;
        chai_1.assert.deepEqual((0, Is_Subsequence_1.isSubsequence)(s, t), expected);
    });
    it("Input: '' 'ahbgdc' - Output: true", () => {
        const s = "";
        const t = "ahbgdc";
        const expected = true;
        chai_1.assert.deepEqual((0, Is_Subsequence_1.isSubsequence)(s, t), expected);
    });
    it("Input: 'abc' '' - Output: false", () => {
        const s = "abc";
        const t = "";
        const expected = false;
        chai_1.assert.deepEqual((0, Is_Subsequence_1.isSubsequence)(s, t), expected);
    });
});
