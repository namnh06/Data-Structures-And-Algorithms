import { assert } from "chai";
import { isSubsequence } from "../../../src/Array-101/Is-Subsequence";

describe("Is Subsequence", function () {
  it("Input: 'abc' 'ahbgdc' - Output: true", () => {
    const s: string = "abc";
    const t: string = "ahbgdc";
    const expected: boolean = true;
    assert.deepEqual(isSubsequence(s, t), expected);
  });

  it("Input: 'axc' 'ahbgdc' - Output: false", () => {
    const s: string = "axc";
    const t: string = "ahbgdc";
    const expected: boolean = false;
    assert.deepEqual(isSubsequence(s, t), expected);
  });

  it("Input: '' 'ahbgdc' - Output: true", () => {
    const s: string = "";
    const t: string = "ahbgdc";
    const expected: boolean = true;
    assert.deepEqual(isSubsequence(s, t), expected);
  });

  it("Input: 'abc' '' - Output: false", () => {
    const s: string = "abc";
    const t: string = "";
    const expected: boolean = false;
    assert.deepEqual(isSubsequence(s, t), expected);
  });
});
