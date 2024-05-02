export function thirdMax(nums: number[]): number | null {
  let arrayLength: number = nums.length;

  // case [1]
  if (arrayLength === 1) {
    return nums[0];
  }

  // case [1,2]
  if (arrayLength === 2) {
    return nums[0] > nums[1] ? nums[0] : nums[1];
  }

  // case [1,2,3]
  let first: number | null = null;
  let second: number | null = null;
  let third: number | null = null;
  for (let i: number = 0; i < arrayLength; i++) {
    if (nums[i] === first || nums[i] === second || nums[i] === third) {
      if (nums[i] === first) {
        first = second;
        second = third;
        third = null;
      }

      if (nums[i] === second) {
        second = third;
        third = null;
      }

      if (nums[i] === third) {
        third = null;
      }
    }

    if (first === null) {
      first = nums[i];
      continue;
    } else {
      if (nums[i] > first) {
        let temp: number = first;
        first = nums[i];
        third = second;
        second = temp;
        continue;
      }
    }

    if (second === null) {
      if (nums[i] > first) {
        [first, second] = swap(first, nums[i]);
      } else {
        second = nums[i];
      }
      continue;
    } else {
      if (nums[i] > second) {
        let temp: number = second;
        second = nums[i];
        third = temp;
        continue;
      }
    }

    if (third === null) {
      if (nums[i] > first) {
        [first, third] = swap(first, nums[i]);
      } else {
        third = nums[i];
      }
    } else {
      if (nums[i] > third) {
        third = nums[i];
      }
    }
  }

  return third !== null ? third : first;
}

function swap(a: number, b: number): number[] {
  let temp: number = a;
  a = b;
  b = temp;
  return [a, b];
}
