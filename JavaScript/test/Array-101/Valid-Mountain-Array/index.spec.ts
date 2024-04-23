import { assert } from "chai";
import { validMountainArray } from "./../../../src/Array-101/Valid-Mountain-Array";

describe("Valid-Mountain-Array", function () {
  it("Input: [2, 1] - Output: false", function () {
    let arr: number[] = [2, 1];
    let expected: boolean = false;
    assert.deepEqual(validMountainArray(arr), expected);
  });

  it("Input: [3, 5, 5] - Output: false", function () {
    let arr: number[] = [3, 5, 5];
    let expected: boolean = false;
    assert.deepEqual(validMountainArray(arr), expected);
  });

  it("Input: [0,3,2,1] - Output: true", function () {
    let arr: number[] = [0, 3, 2, 1];
    let expected: boolean = true;
    assert.deepEqual(validMountainArray(arr), expected);
  });

  it("Input: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - Output: false", function () {
    let arr: number[] = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0];
    let expected: boolean = false;
    assert.deepEqual(validMountainArray(arr), expected);
  });
});
