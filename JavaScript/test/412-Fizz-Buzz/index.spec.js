"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const _412_Fizz_Buzz_1 = require("../../src/412-Fizz-Buzz");
describe('412-Fizz-Buzz', () => {
    it('Input: n = 3 - Output: ["1","2","Fizz"]', () => {
        const result = _412_Fizz_Buzz_1.fizzBuzz.call(null, 3);
        const expected = ["1", "2", "Fizz"];
        chai_1.assert.deepEqual(result, expected);
    });
    it('Input: n = 5 - Output: ["1","2","Fizz","4","Buzz"]', () => {
        const result = _412_Fizz_Buzz_1.fizzBuzz.call(null, 5);
        const expected = ["1", "2", "Fizz", "4", "Buzz"];
        chai_1.assert.deepEqual(result, expected);
    });
    it('Input: n = 15 - Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]', () => {
        const result = _412_Fizz_Buzz_1.fizzBuzz.call(null, 15);
        const expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"];
        chai_1.assert.deepEqual(result, expected);
    });
});
