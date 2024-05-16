export function twoSumSorted(nums: number[], target: number): boolean {
  if (nums.length < 2) {
    return false;
  }

  let left: number = 0;
  let right: number = nums.length - 1;
  while (left < right) {
    const total: number = nums[left] + nums[right];

    if (total < target) {
      left++;
    } else if (total > target) {
      right--;
    } else {
      return true;
    }
  }

  return false;
}
