import { assert } from 'chai';

import { LinkedList } from '../../src/876-Middle-of-the-Linked-List/LinkedList';
import { ListNode } from '../../src/876-Middle-of-the-Linked-List/ListNode';

describe('876-Middle-of-the-Linked-List Linked List Test', function () {
    it('Constructor with null', function () {
        let object = new LinkedList();
        let expected = null;
        assert.deepEqual(object.head, expected);
    });

    it('Constructor with ListNode', function () {
        let val: number = 1;
        let node = new ListNode(val);
        let object = new LinkedList(node);
        let expected = 1;
        assert.deepEqual(object.head?.val, expected);
    });

    it('Add ListNode', function () {
        let val: number = 1;
        let node: ListNode = new ListNode(val);
        let linkedList = new LinkedList();
        linkedList.addNode(node);
        let expected = 1;
        assert.deepEqual(linkedList.head?.val, expected);
    });
});