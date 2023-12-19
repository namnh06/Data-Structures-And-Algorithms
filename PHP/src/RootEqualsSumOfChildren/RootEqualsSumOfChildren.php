<?php

// https://leetcode.com/problems/root-equals-sum-of-children

declare(strict_types=1);

namespace LeetCode\PHP;

class RootEqualsSumOfChildren
{
    public function __construct(
        public int $val = 0,
        public ?RootEqualsSumOfChildren $left = null,
        public ?RootEqualsSumOfChildren $right = null,
    ) {
    }

    public function checkTree(): bool
    {
        return ($this->left->val + $this->right->val) === $this->val;
    }
}
