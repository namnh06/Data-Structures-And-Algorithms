"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Replace_Elements_with_Greatest_Element_on_Right_Side_1 = require("../../../src/Array-101/Replace-Elements-with-Greatest-Element-on-Right-Side");
describe("Replace-Elements-with-Greatest-Element-on-Right-Side", () => {
    it("Input: [] - Output: []", () => {
        let arr = [];
        let expected = [];
        chai_1.assert.deepEqual((0, Replace_Elements_with_Greatest_Element_on_Right_Side_1.replaceElements)(arr), expected);
    });
    it("Input: [200] - Output: [-1]", () => {
        let arr = [200];
        let expected = [-1];
        chai_1.assert.deepEqual((0, Replace_Elements_with_Greatest_Element_on_Right_Side_1.replaceElements)(arr), expected);
    });
    it("Input: [1, 2] - Output: [2, -1]", () => {
        let arr = [1, 2];
        let expected = [2, -1];
        chai_1.assert.deepEqual((0, Replace_Elements_with_Greatest_Element_on_Right_Side_1.replaceElements)(arr), expected);
    });
    it("Input: [17,18,5,4,6,1] - Output: [18,6,6,6,1,-1]", () => {
        let arr = [17, 18, 5, 4, 6, 1];
        let expected = [18, 6, 6, 6, 1, -1];
        chai_1.assert.deepEqual((0, Replace_Elements_with_Greatest_Element_on_Right_Side_1.replaceElements)(arr), expected);
    });
    it("Input: [17,18,5,4,6,1,2] - Output: [18,6,6,6,2,2,-1]", () => {
        let arr = [17, 18, 5, 4, 6, 1, 2];
        let expected = [18, 6, 6, 6, 2, 2, -1];
        chai_1.assert.deepEqual((0, Replace_Elements_with_Greatest_Element_on_Right_Side_1.replaceElements)(arr), expected);
    });
    it("Input: [17,18,5,4,6,1,-1] - Output: [18,6,6,6,1,-1,-1]", () => {
        let arr = [17, 18, 5, 4, 6, 1, -1];
        let expected = [18, 6, 6, 6, 1, -1, -1];
        chai_1.assert.deepEqual((0, Replace_Elements_with_Greatest_Element_on_Right_Side_1.replaceElements)(arr), expected);
    });
    it("Input: [-1, -1, -1] - Output: [-1, -1, -1]", () => {
        let arr = [-1, -1, -1];
        let expected = [-1, -1, -1];
        chai_1.assert.deepEqual((0, Replace_Elements_with_Greatest_Element_on_Right_Side_1.replaceElements)(arr), expected);
    });
});
