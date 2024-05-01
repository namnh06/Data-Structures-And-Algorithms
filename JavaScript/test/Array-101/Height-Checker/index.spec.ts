import { assert } from "chai";
import { heightChecker } from "./../../../src/Array-101/Height-Checker";

describe("Height-Checker", function () {
  it("Input: [1] - Output: 0", () => {
    let heights: number[] = [1];
    let expected: number = 0;
    assert.deepEqual(heightChecker(heights), expected);
  });

  it("Input: [1, 2] - Output: 0", () => {
    let heights: number[] = [1, 2];
    let expected: number = 0;
    assert.deepEqual(heightChecker(heights), expected);
  });

  it("Input: [2, 1] - Output: 2", () => {
    let heights: number[] = [2, 1];
    let expected: number = 2;
    assert.deepEqual(heightChecker(heights), expected);
  });

  it("Input: [1, 2 , 3] - Output: 0", () => {
    let heights: number[] = [1, 2, 3];
    let expected: number = 0;
    assert.deepEqual(heightChecker(heights), expected);
  });

  it("Input: [2, 1 , 2] - Output: 2", () => {
    let heights: number[] = [2, 1, 2];
    let expected: number = 2;
    assert.deepEqual(heightChecker(heights), expected);
  });

  it("Input: [2, 1, 3] - Output: 2", () => {
    let heights: number[] = [2, 1, 3];
    let expected: number = 2;
    assert.deepEqual(heightChecker(heights), expected);
  });

  it("Input: [1,1,4,2,1,3] - Output: 3", () => {
    let heights: number[] = [1, 1, 4, 2, 1, 3];
    let expected: number = 3;
    assert.deepEqual(heightChecker(heights), expected);
  });

  it("Input: [1,2,3,4,5] - Output: 5", () => {
    let heights: number[] = [5, 1, 2, 3, 4];
    let expected: number = 5;
    assert.deepEqual(heightChecker(heights), expected);
  });

  it("Input: [1,2,3,4,5] - Output: 0", () => {
    let heights: number[] = [1, 2, 3, 4, 5];
    let expected: number = 0;
    assert.deepEqual(heightChecker(heights), expected);
  });
});
