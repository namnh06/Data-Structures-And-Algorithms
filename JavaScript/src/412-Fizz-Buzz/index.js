"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.fizzBuzz = void 0;
// https://leetcode.com/problems/fizz-buzz/
function fizzBuzz(n) {
    let result = [];
    for (let index = 1; index <= n; index++) {
        let temporaryString = index.toString();
        if (index % 3 === 0) {
            temporaryString = "Fizz";
        }
        if (index % 5 === 0) {
            if (temporaryString !== "Fizz") {
                temporaryString = "Buzz";
            }
            else {
                temporaryString += "Buzz";
            }
        }
        result.push(temporaryString);
    }
    return result;
}
exports.fizzBuzz = fizzBuzz;
;
