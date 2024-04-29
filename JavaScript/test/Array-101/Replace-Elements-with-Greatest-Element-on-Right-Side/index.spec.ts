import { assert } from "chai";
import { replaceElements } from "../../../src/Array-101/Replace-Elements-with-Greatest-Element-on-Right-Side";

describe("Replace-Elements-with-Greatest-Element-on-Right-Side", () => {
  it("Input: [] - Output: []", () => {
    let arr: number[] = [];
    let expected: number[] = [];
    assert.deepEqual(replaceElements(arr), expected);
  });

  it("Input: [200] - Output: [-1]", () => {
    let arr: number[] = [200];
    let expected: number[] = [-1];
    assert.deepEqual(replaceElements(arr), expected);
  });

  it("Input: [1, 2] - Output: [2, -1]", () => {
    let arr: number[] = [1, 2];
    let expected: number[] = [2, -1];
    assert.deepEqual(replaceElements(arr), expected);
  });

  it("Input: [17,18,5,4,6,1] - Output: [18,6,6,6,1,-1]", () => {
    let arr: number[] = [17, 18, 5, 4, 6, 1];
    let expected: number[] = [18, 6, 6, 6, 1, -1];
    assert.deepEqual(replaceElements(arr), expected);
  });

  it("Input: [17,18,5,4,6,1,2] - Output: [18,6,6,6,2,2,-1]", () => {
    let arr: number[] = [17, 18, 5, 4, 6, 1, 2];
    let expected: number[] = [18, 6, 6, 6, 2, 2, -1];
    assert.deepEqual(replaceElements(arr), expected);
  });

  it("Input: [17,18,5,4,6,1,-1] - Output: [18,6,6,6,1,-1,-1]", () => {
    let arr: number[] = [17, 18, 5, 4, 6, 1, -1];
    let expected: number[] = [18, 6, 6, 6, 1, -1, -1];
    assert.deepEqual(replaceElements(arr), expected);
  });

  it("Input: [-1, -1, -1] - Output: [-1, -1, -1]", () => {
    let arr: number[] = [-1, -1, -1];
    let expected: number[] = [-1, -1, -1];
    assert.deepEqual(replaceElements(arr), expected);
  });
});
