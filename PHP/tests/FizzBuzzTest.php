<?php declare(strict_types=1);
namespace LeetCode\PHP;

use PHPUnit\Framework\TestCase;

final class FizzBuzzTest extends TestCase
{
    public function testClassConstructor(): void
    {
        $input = 3;
        $fizzBuzz = new FizzBuzz($input);
        $result = $fizzBuzz->number;
        $this->assertSame($input, $result);
    }

    public function testFirstCase() : void
    {
        $input = 3;
        $fizzBuzz = new FizzBuzz($input);
        $result = $fizzBuzz->execute();
        $expected = ["1","2","Fizz"];
        $this->assertSame($expected, $result);
    }

    public function testSecondCase() : void
    {
        $input = 5;
        $fizzBuzz = new FizzBuzz($input);
        $result = $fizzBuzz->execute();
        $expected = ["1","2","Fizz","4","Buzz"];
        $this->assertSame($expected, $result);
    }

    public function testThirdCase() : void
    {
        $input = 15;
        $fizzBuzz = new FizzBuzz($input);
        $result = $fizzBuzz->execute();
        $expected = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"];
        $this->assertSame($expected, $result);
    }
}
