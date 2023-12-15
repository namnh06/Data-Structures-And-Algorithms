<?php

declare(strict_types=1);

namespace LeetCode\PHP;

use PHPUnit\Framework\TestCase;

class LinkedListTest extends TestCase
{
    public function testClassConstructor()
    {
        $input = 1;
        $node = new ListNode($input);
        $object = new LinkedList($node);
        $this->assertSame($node, $object->head);
    }
}
