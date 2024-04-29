import { assert } from "chai";
import { removeElement } from "../../../src/Array-101/Remove-Element";

describe("Remove-Elements", function () {
  it("Input: [] - Val Remove: 1 - Output: 0", () => {
    let nums: number[] = [];
    let valRemove: number = 1;
    let expected: number = 0;
    assert.deepEqual(removeElement(nums, valRemove), expected);
  });

  it("Input: [0] - Val Remove: 1 - Output: 1", () => {
    let nums: number[] = [0];
    let valRemove: number = 1;
    let expected: number = 1;
    assert.deepEqual(removeElement(nums, valRemove), expected);
  });

  it("Input: [1] - Val Remove: 1 - Output: 0", () => {
    let nums: number[] = [1];
    let valRemove: number = 1;
    let expected: number = 0;
    assert.deepEqual(removeElement(nums, valRemove), expected);
  });

  it("Input: [1, 1] - Val Remove: 1 - Output: 0", () => {
    let nums: number[] = [1, 1];
    let valRemove: number = 1;
    let expected: number = 0;
    assert.deepEqual(removeElement(nums, valRemove), expected);
  });

  it("Input: [0,1,2,2,3,0,4,2] - Val Remove: 2 - Output: 5", () => {
    let nums: number[] = [0, 1, 2, 2, 3, 0, 4, 2];
    let valRemove: number = 2;
    let expected: number = 5;
    assert.deepEqual(removeElement(nums, valRemove), expected);
  });

  2;
});
