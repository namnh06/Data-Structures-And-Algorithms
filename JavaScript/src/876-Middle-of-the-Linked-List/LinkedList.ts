import { ListNode } from './ListNode';

export class LinkedList {
    head: ListNode | null;

    constructor(head?: ListNode | null) {
        this.head = (head === undefined ? null : head);
    }

    addNode(newNode: ListNode): ListNode {
        if (this.head === null) {
            this.head = newNode;
        } else {
            let current: ListNode = this.head;
            while (current?.next !== null) {
                current = current?.next;
            }
            current.next = newNode;
        }
        return this.head;
    }

    findMiddle(): ListNode | null {
        let middle: ListNode | null = this.head;
        let end: ListNode | null = this.head;
        while (end?.next !== null && end !== null) {
            middle = (middle === null ? null : middle?.next);
            end = (end === null ? null : end?.next?.next);
        }
        return middle;
    }
}