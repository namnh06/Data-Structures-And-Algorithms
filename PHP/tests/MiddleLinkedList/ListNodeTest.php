<?php

declare(strict_types=1);

namespace LeetCode\PHP;

use PHPUnit\Framework\TestCase;

class ListNodeTest extends TestCase
{
    public function testClassConstructor()
    {
        $input = 5;
        $object = new ListNode($input);
        $this->assertSame($input, $object->value);
        $this->assertNull($object->next);
    }
}
