export function sortedSquares(nums: number[]): number[] {
  const len: number = nums.length;
  if (len === 1) {
    return [Math.pow(nums[0], 2)];
  }

  let pointer: number = len - 1;
  let result: number[] = new Array();
  for (let index: number = 0; index <= pointer; index++) {
    const numIndexSquare: number = Math.pow(nums[index], 2);
    const numPointerSquare: number = Math.pow(nums[pointer], 2);

    if (numIndexSquare > numPointerSquare) {
      result.unshift(numIndexSquare);
    } else {
      result.unshift(numPointerSquare);
      pointer--;
      index--;
    }
  }

  return result;
}
