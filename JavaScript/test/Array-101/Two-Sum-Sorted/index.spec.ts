import { assert } from "chai";
import { twoSumSorted } from "../../../src/Array-101/Two-Sum-Sorted";

describe("Two Sum Sorted", function () {
  it("Input: [0], 1 - Output: false", () => {
    const nums: number[] = [0];
    const target: number = 4;
    const expected: boolean = false;
    assert.deepEqual(twoSumSorted(nums, target), expected);
  });

  it("Input: [1, 2], 4 - Output: false", () => {
    const nums: number[] = [1, 2];
    const target: number = 4;
    const expected: boolean = false;
    assert.deepEqual(twoSumSorted(nums, target), expected);
  });

  it("Input: [1, 2, 4, 6, 8], 13 - Output: false", () => {
    const nums: number[] = [1, 2, 4, 6, 8];
    const target: number = 13;
    const expected: boolean = false;
    assert.deepEqual(twoSumSorted(nums, target), expected);
  });

  it("Input: [1, 2, 4, 6, 8, 9, 14, 15], 13 - Output: true", () => {
    const nums: number[] = [1, 2, 4, 6, 8, 9, 14, 15];
    const target: number = 13;
    const expected: boolean = true;
    assert.deepEqual(twoSumSorted(nums, target), expected);
  });
});
