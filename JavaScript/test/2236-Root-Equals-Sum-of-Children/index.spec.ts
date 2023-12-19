import { assert } from 'chai';

import { TreeNode, checkTree } from './../../src/2236-Root-Equals-Sum-of-Children';

describe('2236-Root-Equals-Sum-of-Children', function () {
    it('Class Constructor', function () {
        let object: TreeNode = new TreeNode(10);
        let expected: number = 10;
        assert.deepEqual(object.val, expected);
    });

    it('Input: root = [10, 4, 6] - Output: true', function () {
        let object: TreeNode = new TreeNode(10, new TreeNode(4), new TreeNode(6));
        let expected: boolean = true;
        assert.deepEqual(checkTree(object), expected);
    });

    it('Input: root = [5, 3, 1] - Output: false', function () {
        let object: TreeNode = new TreeNode(5, new TreeNode(3), new TreeNode(1));
        let expected: boolean = false;
        assert.deepEqual(checkTree(object), expected);
    });
});