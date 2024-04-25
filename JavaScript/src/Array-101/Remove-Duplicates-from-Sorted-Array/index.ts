export function removeDuplicates(nums: number[]): number {
  // better, using pointer
  let k = 1;
  for (let i = k; i < nums.length; i++) {
    if (nums[i] !== nums[i - 1]) {
      nums[k++] = nums[i];
    }
  }

  return k;
  //   let length: number = nums.length;
  //   if (length === 1 || nums[0] === nums[length - 1]) {
  //     return 1;
  //   }

  //   for (let i: number = 0; i < length; i++) {
  //     if (nums[i] === nums[i + 1]) {
  //       for (let j: number = i + 1; j < length; j++) {
  //         nums[j] = nums[j + 1];
  //       }
  //       length--;
  //       i--;
  //     }
  //   }
  //   return length;
}
