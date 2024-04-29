import { assert } from "chai";
import { moveZeroes } from "../../../src/Array-101/Move-Zeroes";

describe("Move-Zeroes", function () {
  it("Input: [0] - Output: [0]", () => {
    let arr: number[] = [0];
    let expected: number[] = [0];
    assert.deepEqual(moveZeroes(arr), expected);
  });

  it("Input: [0, 1, 0, 3, 12] - Output: [1, 3, 12, 0, 0]", () => {
    let arr: number[] = [0, 1, 0, 3, 12];
    let expected: number[] = [1, 3, 12, 0, 0];
    assert.deepEqual(moveZeroes(arr), expected);
  });

  it("Input: [0, 0, 0] - Output: [0, 0, 0]", () => {
    let arr: number[] = [0, 0, 0];
    let expected: number[] = [0, 0, 0];
    assert.deepEqual(moveZeroes(arr), expected);
  });
});
