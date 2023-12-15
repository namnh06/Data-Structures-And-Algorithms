<?php

declare(strict_types=1);

namespace LeetCode\PHP;

class ListNode
{
    public $value = 0;
    public $next = null;

    public function __construct($value = 0, $next = null)
    {
        $this->value = $value;
        $this->next = $next;
    }
}
