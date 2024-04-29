import { assert } from "chai";
import { sortArrayByParity } from "../../../src/Array-101/Sort-Array-By-Parity";

describe("Sort-Array-By-Parity", function () {
  it("Input: [0] - Output: [0]", () => {
    let nums: number[] = [0];
    let expected: number[] = [0];
    assert.deepEqual(sortArrayByParity(nums), expected);
  });

  it("Input: [4, 3, 1, 2] - Output: [4, 2, 1, 3]", () => {
    let nums: number[] = [4, 3, 1, 2];
    let expected: number[] = [4, 2, 1, 3];
    assert.deepEqual(sortArrayByParity(nums), expected);
  });
});
