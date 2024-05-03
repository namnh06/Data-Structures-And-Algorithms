import { assert } from "chai";
import { findDisappearedNumbers } from "../../../src/Array-101/Find-All-Numbers-Disappeared-in-an-Array";

describe("Find-All-Numbers-Disappeared-in-an-Array", function () {
  it("Input: [1, 1] - Output: [2]", () => {
    let nums: number[] = [1, 1];
    let expected: number[] = [2];
    assert.deepEqual(findDisappearedNumbers(nums), expected);
  });

  it("Input: [2, 2] - Output: [1]", () => {
    let nums: number[] = [2, 2];
    let expected: number[] = [1];
    assert.deepEqual(findDisappearedNumbers(nums), expected);
  });

  it("Input: [4,3,2,7,8,2,3,1] - Output: [5, 6]", () => {
    let nums: number[] = [4, 3, 2, 7, 8, 2, 3, 1];
    let expected: number[] = [5, 6];
    assert.deepEqual(findDisappearedNumbers(nums), expected);
  });
});
