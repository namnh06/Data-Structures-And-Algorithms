import { assert } from "chai";
import { maximumWealth } from "../../../src/Array-101/1672-Richest-Customer-Wealth";

describe("1672. Richest Customer Wealth", () => {
  it("Input: [[1,2,3],[3,2,1]] - Output: 6", () => {
    const result = maximumWealth.call(null, [
      [1, 2, 3],
      [3, 2, 1],
    ]);
    assert.deepEqual(result, 6);
  });

  it("Input: [[1,5],[7,3],[3,5]] - Output: 10", () => {
    const result = maximumWealth.call(null, [
      [1, 5],
      [7, 3],
      [3, 5],
    ]);
    assert.deepEqual(result, 10);
  });

  it("Input: [[2,8,7],[7,1,3],[1,9,5]] - Output: 17", () => {
    const result = maximumWealth.call(null, [
      [2, 8, 7],
      [7, 1, 3],
      [1, 9, 5],
    ]);
    assert.deepEqual(result, 17);
  });
});
