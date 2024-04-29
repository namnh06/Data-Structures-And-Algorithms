export function removeElement(nums: number[], val: number): number {
  // smarter solution
  let index: number = 0;
  let length: number = nums.length;

  while (index < length) {
    if (nums[index] === val) {
      nums[index] = nums[--length];
    } else {
      index++;
    }
  }

  return length;

  // original
  //   let k: number = 0;
  //   let lengthNums: number = nums.length;
  //   if (lengthNums <= 1) {
  //     if (lengthNums === 1 && nums[0] !== val) {
  //       return 1;
  //     }
  //     return k;
  //   }
  //   for (let i: number = 0; i < lengthNums; i++) {
  //     if (nums[i] !== val) {
  //       nums[k] = nums[i];
  //       if (i !== k++) {
  //         nums[i] = val;
  //       }
  //     }
  //   }
  //   return k;
}
