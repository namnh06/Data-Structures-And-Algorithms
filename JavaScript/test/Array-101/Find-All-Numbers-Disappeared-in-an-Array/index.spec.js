"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const Find_All_Numbers_Disappeared_in_an_Array_1 = require("../../../src/Array-101/Find-All-Numbers-Disappeared-in-an-Array");
describe("Find-All-Numbers-Disappeared-in-an-Array", function () {
    it("Input: [1, 1] - Output: [2]", () => {
        let nums = [1, 1];
        let expected = [2];
        chai_1.assert.deepEqual((0, Find_All_Numbers_Disappeared_in_an_Array_1.findDisappearedNumbers)(nums), expected);
    });
    it("Input: [2, 2] - Output: [1]", () => {
        let nums = [2, 2];
        let expected = [1];
        chai_1.assert.deepEqual((0, Find_All_Numbers_Disappeared_in_an_Array_1.findDisappearedNumbers)(nums), expected);
    });
    it("Input: [4,3,2,7,8,2,3,1] - Output: [5, 6]", () => {
        let nums = [4, 3, 2, 7, 8, 2, 3, 1];
        let expected = [5, 6];
        chai_1.assert.deepEqual((0, Find_All_Numbers_Disappeared_in_an_Array_1.findDisappearedNumbers)(nums), expected);
    });
});
