import { assert } from "chai";
import { sortedSquares } from "../../../src/Array-101/Squares-of-a-Sorted-Array";

describe("Squares of a Sorted Array", function () {
  it("Input: [0] - Output: [0]", () => {
    let nums: number[] = [0];
    let expected: number[] = [0];
    assert.deepEqual(sortedSquares(nums), expected);
  });

  it("Input: [-2, 1] - Output: [1, 4]", () => {
    let nums: number[] = [-2, 1];
    let expected: number[] = [1, 4];
    assert.deepEqual(sortedSquares(nums), expected);
  });

  it("Input: [-4, -1, 0, 3, 10] - Output: [0, 1, 9, 16, 100]", () => {
    let nums: number[] = [-4, -1, 0, 3, 10];
    let expected: number[] = [0, 1, 9, 16, 100];
    assert.deepEqual(sortedSquares(nums), expected);
  });
});
