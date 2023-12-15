<?php

// https://leetcode.com/problems/fizz-buzz/
declare(strict_types=1);

namespace LeetCode\PHP;

class NumberOfSteps
{
    public int $number;

    public function __construct(int $number)
    {
        $this->number = $number;
    }

    public function execute(): int
    {
        $step = 0;
        while($this->number > 0) {
            if($this->number % 2 !== 0) {
                $this->number--;
            } else {
                $this->number /= 2;
            }
            $step++;
        }
        return $step;
    }
}
