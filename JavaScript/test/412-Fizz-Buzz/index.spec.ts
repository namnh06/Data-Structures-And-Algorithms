import { assert } from 'chai';
import { fizzBuzz } from '../../src/412-Fizz-Buzz';

describe('412-Fizz-Buzz', () => {
    it('Input: n = 3 - Output: ["1","2","Fizz"]', () => {
        const result = fizzBuzz.call(null, 3);
        const expected = ["1", "2", "Fizz"];
        assert.deepEqual(result, expected);
    });

    it('Input: n = 5 - Output: ["1","2","Fizz","4","Buzz"]', () => {
        const result = fizzBuzz.call(null, 5);
        const expected = ["1", "2", "Fizz", "4", "Buzz"];
        assert.deepEqual(result, expected);
    });

    it('Input: n = 15 - Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]',
        () => {
            const result = fizzBuzz.call(null, 15);
            const expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"];
            assert.deepEqual(result, expected);
        });
})