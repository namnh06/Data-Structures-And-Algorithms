// https://leetcode.com/problems/running-sum-of-1d-array/
export function runningSum(nums: number[]): number[] {
    let result: number[] = [];
    let previousSum: number = 0;
    nums.forEach(function (num, index) {
        result[index] = previousSum += num;
    });
    return result;
}