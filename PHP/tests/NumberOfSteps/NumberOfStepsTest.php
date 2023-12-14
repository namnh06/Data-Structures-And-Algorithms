<?php 
// https://leetcode.com/problems/fizz-buzz/
declare(strict_types=1);
namespace LeetCode\PHP;

use PHPUnit\Framework\TestCase;

final class NumberOfStepsTest extends TestCase
{
    public function testClassConstructor(): void 
    {
        $input = 3;
        $object = new NumberOfSteps($input);
        $this->assertSame($input, $object->number);
    }

    public function testFirstCase(): void
    {
        $input = 14;
        $result = (new NumberOfSteps($input))->execute();
        $expected = 6;
        $this->assertSame($expected, $result);
    }

    public function testSecondCase(): void
    {
        $input = 8;
        $result = (new NumberOfSteps($input))->execute();
        $expected = 4;
        $this->assertSame($expected, $result);
    }

    public function testThirdCase(): void
    {
        $input = 123;
        $result = (new NumberOfSteps($input))->execute();
        $expected = 12;
        $this->assertSame($expected, $result);
    }
}