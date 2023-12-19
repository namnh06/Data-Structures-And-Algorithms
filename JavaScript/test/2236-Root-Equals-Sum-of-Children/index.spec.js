"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const _2236_Root_Equals_Sum_of_Children_1 = require("./../../src/2236-Root-Equals-Sum-of-Children");
describe('2236-Root-Equals-Sum-of-Children', function () {
    it('Class Constructor', function () {
        let object = new _2236_Root_Equals_Sum_of_Children_1.TreeNode(10);
        let expected = 10;
        chai_1.assert.deepEqual(object.val, expected);
    });
    it('Input: root = [10, 4, 6] - Output: true', function () {
        let object = new _2236_Root_Equals_Sum_of_Children_1.TreeNode(10, new _2236_Root_Equals_Sum_of_Children_1.TreeNode(4), new _2236_Root_Equals_Sum_of_Children_1.TreeNode(6));
        let expected = true;
        chai_1.assert.deepEqual((0, _2236_Root_Equals_Sum_of_Children_1.checkTree)(object), expected);
    });
    it('Input: root = [5, 3, 1] - Output: false', function () {
        let object = new _2236_Root_Equals_Sum_of_Children_1.TreeNode(5, new _2236_Root_Equals_Sum_of_Children_1.TreeNode(3), new _2236_Root_Equals_Sum_of_Children_1.TreeNode(1));
        let expected = false;
        chai_1.assert.deepEqual((0, _2236_Root_Equals_Sum_of_Children_1.checkTree)(object), expected);
    });
});
