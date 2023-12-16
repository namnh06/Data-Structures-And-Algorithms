"use strict";
// https://leetcode.com/problems/middle-of-the-linked-list
Object.defineProperty(exports, "__esModule", { value: true });
exports.generateLinkedList = exports.middleNode = void 0;
const ListNode_1 = require("./ListNode");
const LinkedList_1 = require("./LinkedList");
function middleNode(head) {
    return head.findMiddle();
}
exports.middleNode = middleNode;
function generateLinkedList(num) {
    let index = 1;
    let head = new LinkedList_1.LinkedList(null);
    while (index <= num) {
        let node = new ListNode_1.ListNode(index);
        head.addNode(node);
        index++;
    }
    return head;
}
exports.generateLinkedList = generateLinkedList;
