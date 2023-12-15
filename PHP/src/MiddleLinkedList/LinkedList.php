<?php

declare(strict_types=1);

namespace LeetCode\PHP;

class LinkedList
{
    public ?ListNode $head;

    public function __construct(?ListNode $node = null)
    {
        $this->head = $node;
    }

    public function addNode(ListNode $newNode): void
    {
        if($this->head === null) {
            $this->head = $newNode;
        } else {
            $current = $this->head;
            while($current->next !== null) {
                $current = $current->next;
            }
            $current->next = $newNode;
        }
    }

    public function displayList(): void
    {
        $current = $this->head;
        while($current !== null) {
            echo $current->value . " -> ";
            $current = $current->next;
        }
    }

    public function findMiddle(): ListNode
    {
        $middle = $this->head;
        $move = $this->head;
        while(!is_null($move) && !is_null($move->next)) {
            $middle = $middle->next;
            $move = $move->next->next;
        }
        return $middle;
    }
}
