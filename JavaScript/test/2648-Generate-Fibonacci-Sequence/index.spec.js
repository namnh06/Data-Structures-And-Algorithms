"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const chai_1 = require("chai");
const _2648_Generate_Fibonacci_Sequence_1 = require("../../src/2648-Generate-Fibonacci-Sequence");
describe("Generate Fibonacci Sequence", function () {
    it("Input: callCount 5 - Output: [0,1,1,2,3]", () => {
        let result = [];
        const gen = (0, _2648_Generate_Fibonacci_Sequence_1.fibGenerator)();
        result.push(gen.next().value);
        result.push(gen.next().value);
        result.push(gen.next().value);
        result.push(gen.next().value);
        result.push(gen.next().value);
        chai_1.assert.deepEqual(result, [0, 1, 1, 2, 3]);
    });
});
