<?php

// https://leetcode.com/problems/root-equals-sum-of-children

declare(strict_types=1);

namespace LeetCode\PHP;

use PHPUnit\Framework\TestCase;

final class RootEqualsSumOfChildrenTest extends TestCase
{
    public function testClassConstructor(): void
    {
        $object = new RootEqualsSumOfChildren(10);
        $this->assertSame(10, $object->val);
    }

    public function testCaseTrue(): void
    {
        $object = new RootEqualsSumOfChildren(
            10,
            new RootEqualsSumOfChildren(4),
            new RootEqualsSumOfChildren(6),
        );
        $this->assertSame(true, $object->checkTree());
    }

    public function testCaseFalse(): void
    {
        $object = new RootEqualsSumOfChildren(
            5,
            new RootEqualsSumOfChildren(3),
            new RootEqualsSumOfChildren(1),
        );
        $this->assertSame(false, $object->checkTree());
    }
}
