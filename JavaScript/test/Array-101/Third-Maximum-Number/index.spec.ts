import { assert } from "chai";
import { thirdMax } from "../../../src/Array-101/Third-Maximum-Number";

describe("Third-Maximum-Number", function () {
  it("Input: [1] - Output: 1", () => {
    let nums: number[] = [1];
    let expected: number = 1;
    assert.deepEqual(thirdMax(nums), expected);
  });

  it("Input: [1, 2] - Output: 2", () => {
    let nums: number[] = [1, 2];
    let expected: number = 2;
    assert.deepEqual(thirdMax(nums), expected);
  });

  it("Input: [1, 2, 3] - Output: 1", () => {
    let nums: number[] = [1, 2, 3];
    let expected: number = 1;
    assert.deepEqual(thirdMax(nums), expected);
  });

  it("Input: [1, -1, 3] - Output: -1", () => {
    let nums: number[] = [1, -1, 3];
    let expected: number = -1;
    assert.deepEqual(thirdMax(nums), expected);
  });

  it("Input: [5, 2, 1, 3, 0, 6, 4] - Output: 4", () => {
    let nums: number[] = [5, 2, 1, 3, 0, 6, 4];
    let expected: number = 4;
    assert.deepEqual(thirdMax(nums), expected);
  });
});
