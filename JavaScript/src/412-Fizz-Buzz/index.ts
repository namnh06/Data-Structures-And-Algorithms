// https://leetcode.com/problems/fizz-buzz/
export function fizzBuzz(n: number): string[] {
    let result: string[] = [];

    for (let index = 1; index <= n; index++) {
        let temporaryString: string = index.toString();

        if (index % 3 === 0) {
            temporaryString = "Fizz";
        }

        if (index % 5 === 0) {
            if (temporaryString !== "Fizz") {
                temporaryString = "Buzz";
            } else {
                temporaryString += "Buzz";
            }
        }

        result.push(temporaryString);
    }

    return result;
};