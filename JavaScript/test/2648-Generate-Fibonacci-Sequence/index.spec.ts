import { assert } from "chai";
import { fibGenerator } from "../../src/2648-Generate-Fibonacci-Sequence";

describe("Generate Fibonacci Sequence", function () {
  it("Input: callCount 5 - Output: [0,1,1,2,3]", () => {
    let result: number[] = [];
    const gen = fibGenerator();
    result.push(gen.next().value);
    result.push(gen.next().value);
    result.push(gen.next().value);
    result.push(gen.next().value);
    result.push(gen.next().value);
    assert.deepEqual(result, [0, 1, 1, 2, 3]);
  });
});
