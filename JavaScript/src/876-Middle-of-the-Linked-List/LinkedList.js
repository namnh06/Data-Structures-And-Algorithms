"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.LinkedList = void 0;
class LinkedList {
    constructor(head) {
        this.head = (head === undefined ? null : head);
    }
    addNode(newNode) {
        if (this.head === null) {
            this.head = newNode;
        }
        else {
            let current = this.head;
            while ((current === null || current === void 0 ? void 0 : current.next) !== null) {
                current = current === null || current === void 0 ? void 0 : current.next;
            }
            current.next = newNode;
        }
        return this.head;
    }
    findMiddle() {
        var _a;
        let middle = this.head;
        let end = this.head;
        while ((end === null || end === void 0 ? void 0 : end.next) !== null && end !== null) {
            middle = (middle === null ? null : middle === null || middle === void 0 ? void 0 : middle.next);
            end = (end === null ? null : (_a = end === null || end === void 0 ? void 0 : end.next) === null || _a === void 0 ? void 0 : _a.next);
        }
        return middle;
    }
}
exports.LinkedList = LinkedList;
