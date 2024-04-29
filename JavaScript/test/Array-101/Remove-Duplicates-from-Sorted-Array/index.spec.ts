import { assert } from "chai";
import { removeDuplicates } from "../../../src/Array-101/Remove-Duplicates-from-Sorted-Array";

describe("Remove-Duplicates-from-Sorted-Array", function () {
  it("Input: [1] - Output: 1", function () {
    let arr: number[] = [1];
    let expected: number = 1;
    assert.deepEqual(removeDuplicates(arr), expected);
  });

  it("Input: [1, 1, 1, 1] - Output: 1", function () {
    let arr: number[] = [1, 1, 1, 1];
    let expected: number = 1;
    assert.deepEqual(removeDuplicates(arr), expected);
  });

  it("Input: [1, 2] - Output: 2", function () {
    let arr: number[] = [1, 2];
    let expected: number = 2;
    assert.deepEqual(removeDuplicates(arr), expected);
  });

  it("Input: [1, 2, 2] - Output: 2", function () {
    let arr: number[] = [1, 2, 2];
    let expected: number = 2;
    assert.deepEqual(removeDuplicates(arr), expected);
  });

  it("Input: [1, 1, 2, 2] - Output: 2", function () {
    let arr: number[] = [1, 1, 2, 2];
    let expected: number = 2;
    assert.deepEqual(removeDuplicates(arr), expected);
  });

  it("Input: [1, 1, 2, 2, 3] - Output: 3", function () {
    let arr: number[] = [1, 1, 2, 2, 3];
    let expected: number = 3;
    assert.deepEqual(removeDuplicates(arr), expected);
  });

  it("Input: [1, 1, 1, 2, 2, 3] - Output: 3", function () {
    let arr: number[] = [1, 1, 1, 2, 2, 3];
    let expected: number = 3;
    assert.deepEqual(removeDuplicates(arr), expected);
  });
});
