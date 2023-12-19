"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.checkTree = exports.TreeNode = void 0;
// https://leetcode.com/problems/root-equals-sum-of-children
class TreeNode {
    constructor(val, left, right) {
        this.val = (val === undefined ? 0 : val);
        this.left = (left === undefined ? null : left);
        this.right = (right === undefined ? null : right);
    }
}
exports.TreeNode = TreeNode;
function checkTree(root) {
    var _a, _b;
    if (root === null || (root === null || root === void 0 ? void 0 : root.left) === null || (root === null || root === void 0 ? void 0 : root.right) === null) {
        return false;
    }
    return (((_a = root === null || root === void 0 ? void 0 : root.left) === null || _a === void 0 ? void 0 : _a.val) + ((_b = root === null || root === void 0 ? void 0 : root.right) === null || _b === void 0 ? void 0 : _b.val)) === (root === null || root === void 0 ? void 0 : root.val);
}
exports.checkTree = checkTree;
