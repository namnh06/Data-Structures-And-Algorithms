// https://leetcode.com/problems/middle-of-the-linked-list

import { ListNode } from './ListNode';
import { LinkedList } from './LinkedList';

export function middleNode(head: LinkedList): ListNode | null {
    return head.findMiddle();
}

export function generateLinkedList(num: number): LinkedList {
    let index: number = 1;
    let head: LinkedList = new LinkedList(null);
    while (index <= num) {
        let node: ListNode = new ListNode(index);
        head.addNode(node);
        index++;
    }
    return head;
}