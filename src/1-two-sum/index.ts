// https://leetcode.com/problems/two-sum/
export function twoSum(nums: number[], target: number): number[] | void {
    for (let i: number = 1; i < nums.length; i++) {
        const total: number = nums[i - 1] + nums[i];
        if (total == target) return [i - 1, i];

        for (let j: number = 0; j < i; j++) {
            const nextTotal: number = nums[j] + nums[i];
            if (nextTotal == target) return [j, i];
        }
    }
};