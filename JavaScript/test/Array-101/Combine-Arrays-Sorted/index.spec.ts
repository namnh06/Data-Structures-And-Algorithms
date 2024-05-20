import { assert } from "chai";
import { combineArraysSorted } from "../../../src/Array-101/Combine-Arrays-Sorted";

describe("Combine Arrays Sorted", function () {
  it("Input: [] [1, 2, 3] - Output: [1, 2, 3]", () => {
    const firstArray: number[] = [];
    const secondArray: number[] = [1, 2, 3];
    const expected: number[] = [1, 2, 3];
    assert.deepEqual(combineArraysSorted(firstArray, secondArray), expected);
  });

  it("Input: [1, 2, 2] [] - Output: [1, 2, 2]", () => {
    const firstArray: number[] = [1, 2, 2];
    const secondArray: number[] = [];
    const expected: number[] = [1, 2, 2];
    assert.deepEqual(combineArraysSorted(firstArray, secondArray), expected);
  });

  it("Input: [1] [2] - Output: [1, 2]", () => {
    const firstArray: number[] = [1];
    const secondArray: number[] = [2];
    const expected: number[] = [1, 2];
    assert.deepEqual(combineArraysSorted(firstArray, secondArray), expected);
  });

  it("Input: [1, 2] [2] - Output: [1, 2, 2]", () => {
    const firstArray: number[] = [1, 2];
    const secondArray: number[] = [2];
    const expected: number[] = [1, 2, 2];
    assert.deepEqual(combineArraysSorted(firstArray, secondArray), expected);
  });

  it("Input: [1, 2] [2, 4] - Output: [1, 2, 2, 4]", () => {
    const firstArray: number[] = [1, 2];
    const secondArray: number[] = [2, 4];
    const expected: number[] = [1, 2, 2, 4];
    assert.deepEqual(combineArraysSorted(firstArray, secondArray), expected);
  });

  it("Input: [1, 2] [2, 4, 5] - Output: [1, 2, 2, 4, 5]", () => {
    const firstArray: number[] = [1, 2];
    const secondArray: number[] = [2, 4, 5];
    const expected: number[] = [1, 2, 2, 4, 5];
    assert.deepEqual(combineArraysSorted(firstArray, secondArray), expected);
  });

  it("Input: [1, 2, 6] [2, 4, 5] - Output: [1, 2, 2, 4, 5, 6]", () => {
    const firstArray: number[] = [1, 2, 6];
    const secondArray: number[] = [2, 4, 5];
    const expected: number[] = [1, 2, 2, 4, 5, 6];
    assert.deepEqual(combineArraysSorted(firstArray, secondArray), expected);
  });
});
