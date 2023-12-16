import { assert } from 'chai';

import { ListNode } from '../../src/876-Middle-of-the-Linked-List/ListNode';

describe('876-Middle-of-the-Linked-List List Node Test', function () {
    it('Constructor', function () {
        const object = new ListNode(1);
        const expected = 1;
        assert.deepEqual(object.val, expected);
    });
});