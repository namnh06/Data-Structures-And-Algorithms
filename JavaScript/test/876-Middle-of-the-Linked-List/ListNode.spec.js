"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const ListNode_1 = require("../../src/876-Middle-of-the-Linked-List/ListNode");
describe('876-Middle-of-the-Linked-List List Node Test', function () {
    it('Constructor', function () {
        const object = new ListNode_1.ListNode(1);
        const expected = 1;
        chai_1.assert.deepEqual(object.val, expected);
    });
});
