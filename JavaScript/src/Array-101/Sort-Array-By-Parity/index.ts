export function sortArrayByParity(nums: number[]): number[] {
  let length: number = nums.length;
  if (length < 2) {
    return nums;
  }

  let pointer: number = 0;
  for (let i: number = 0; i < length; i++) {
    let isEven: boolean = nums[i] % 2 === 0;
    if (isEven) {
      let temp: number = nums[i];
      if (pointer !== i) {
        nums[i] = nums[pointer];
      }
      nums[pointer++] = temp;
    }
  }
  return nums;
}
