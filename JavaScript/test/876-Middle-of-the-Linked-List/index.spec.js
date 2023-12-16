"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// https://leetcode.com/problems/middle-of-the-linked-list
const chai_1 = require("chai");
const _876_Middle_of_the_Linked_List_1 = require("../../src/876-Middle-of-the-Linked-List");
const LinkedList_1 = require("../../src/876-Middle-of-the-Linked-List/LinkedList");
const ListNode_1 = require("../../src/876-Middle-of-the-Linked-List/ListNode");
describe('876-Middle-of-the-Linked-List', function () {
    it('generate Linked List', function () {
        let object = (0, _876_Middle_of_the_Linked_List_1.generateLinkedList)(1);
        let node = new ListNode_1.ListNode(1);
        let expected = new LinkedList_1.LinkedList(node);
        chai_1.assert.deepEqual(object, expected);
    });
    it('find middle first case', function () {
        let linkedList = (0, _876_Middle_of_the_Linked_List_1.generateLinkedList)(5);
        let result = (0, _876_Middle_of_the_Linked_List_1.middleNode)(linkedList);
        let expected = 3;
        chai_1.assert.deepEqual(result === null || result === void 0 ? void 0 : result.val, expected);
    });
    it('find middle second case', function () {
        let linkedList = (0, _876_Middle_of_the_Linked_List_1.generateLinkedList)(6);
        let result = (0, _876_Middle_of_the_Linked_List_1.middleNode)(linkedList);
        let expected = 4;
        chai_1.assert.deepEqual(result === null || result === void 0 ? void 0 : result.val, expected);
    });
});
