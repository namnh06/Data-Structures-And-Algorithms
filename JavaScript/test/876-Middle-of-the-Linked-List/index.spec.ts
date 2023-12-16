// https://leetcode.com/problems/middle-of-the-linked-list
import { assert } from 'chai';
import { generateLinkedList, middleNode } from '../../src/876-Middle-of-the-Linked-List';
import { LinkedList } from '../../src/876-Middle-of-the-Linked-List/LinkedList';
import { ListNode } from '../../src/876-Middle-of-the-Linked-List/ListNode';

describe('876-Middle-of-the-Linked-List', function () {
    it('generate Linked List', function () {
        let object: LinkedList = generateLinkedList(1);
        let node: ListNode = new ListNode(1);
        let expected: LinkedList = new LinkedList(node);
        assert.deepEqual(object, expected);
    });

    it('find middle first case', function () {
        let linkedList: LinkedList = generateLinkedList(5);
        let result: ListNode | null = middleNode(linkedList);
        let expected: number = 3;
        assert.deepEqual(result?.val, expected);
    });

    it('find middle second case', function () {
        let linkedList: LinkedList = generateLinkedList(6);
        let result: ListNode | null = middleNode(linkedList);
        let expected: number = 4;
        assert.deepEqual(result?.val, expected);
    });
});
