<?php

// https://leetcode.com/problems/middle-of-the-linked-list
declare(strict_types=1);

namespace LeetCode\PHP;

class MiddleLinkedList
{
    public ?LinkedList $list;

    public function __construct(int $number)
    {
        $this->list = new LinkedList(null);
        foreach($this->generateLinkedList($number) as $key => $value) {
            $this->list->addNode($value);
        }
    }

    private function generateLinkedList(int $number)
    {
        $index = 1;
        while ($index <= $number) {
            $node = new ListNode($index);
            yield $node;
            $index++;
        }
    }
}
