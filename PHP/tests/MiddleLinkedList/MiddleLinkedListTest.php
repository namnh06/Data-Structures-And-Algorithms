<?php

declare(strict_types=1);

namespace LeetCode\PHP;

use PHPUnit\Framework\TestCase;

class MiddleLinkedListTest extends TestCase
{
    public function testClassConstructor(): void
    {
        $input = 5;
        $object = new MiddleLinkedList($input);
        $this->assertSame(1, $object->list->head->value);
    }

    public function testFirstCase(): void
    {
        $input = 5;
        $object = new MiddleLinkedList($input);
        $output = $object->list->findMiddle()->value;
        $expected = 3;
        $this->assertSame($output, $expected);
    }

    public function testSecondCase(): void
    {
        $input = 6;
        $object = new MiddleLinkedList($input);
        $output = $object->list->findMiddle()->value;
        $expected = 4;
        $this->assertSame($output, $expected);
    }
}
