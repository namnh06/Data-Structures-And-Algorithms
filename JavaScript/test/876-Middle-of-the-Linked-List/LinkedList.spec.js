"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const LinkedList_1 = require("../../src/876-Middle-of-the-Linked-List/LinkedList");
const ListNode_1 = require("../../src/876-Middle-of-the-Linked-List/ListNode");
describe('876-Middle-of-the-Linked-List Linked List Test', function () {
    it('Constructor with null', function () {
        let object = new LinkedList_1.LinkedList();
        let expected = null;
        chai_1.assert.deepEqual(object.head, expected);
    });
    it('Constructor with ListNode', function () {
        var _a;
        let val = 1;
        let node = new ListNode_1.ListNode(val);
        let object = new LinkedList_1.LinkedList(node);
        let expected = 1;
        chai_1.assert.deepEqual((_a = object.head) === null || _a === void 0 ? void 0 : _a.val, expected);
    });
    it('Add ListNode', function () {
        var _a;
        let val = 1;
        let node = new ListNode_1.ListNode(val);
        let linkedList = new LinkedList_1.LinkedList();
        linkedList.addNode(node);
        let expected = 1;
        chai_1.assert.deepEqual((_a = linkedList.head) === null || _a === void 0 ? void 0 : _a.val, expected);
    });
});
