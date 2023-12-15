<?php

// https://leetcode.com/problems/fizz-buzz/
declare(strict_types=1);

namespace LeetCode\PHP;

class FizzBuzz
{
    public int $number;

    public function __construct(int $number)
    {
        $this->number = $number;
    }

    public function execute(): array
    {
        $result = [];
        for($index = 1; $index <= $this->number; $index++) {
            $temporaryString = (string)$index;

            if($index % 3 === 0) {
                $temporaryString = "Fizz";
            }

            if($index % 5 === 0) {
                if($temporaryString !== "Fizz") {
                    $temporaryString = "Buzz";
                } else {
                    $temporaryString .= "Buzz";
                }
            }

            $result[] = $temporaryString;
        }

        return $result;
    }
}
