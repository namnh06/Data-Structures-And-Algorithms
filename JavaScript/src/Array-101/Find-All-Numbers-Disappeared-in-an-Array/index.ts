export function findDisappearedNumbers(nums: number[]): number[] {
  let numsLength: number = nums.length;
  let result: number[] = [];
  let numsSorted: number[] = quickSort(nums);
  let firstElement: number = numsSorted[0];
  let lastElement: number = numsSorted[numsLength - 1];

  if (firstElement > 1) {
    for (let i: number = 1; i < firstElement; i++) {
      result.push(i);
    }
  }

  if (lastElement < numsLength) {
    for (let i: number = numsLength; i > lastElement; i--) {
      result.push(i);
    }
  }

  if (numsLength > 2) {
    for (let i: number = 1; i < numsLength; i++) {
      let diff: number = numsSorted[i] - numsSorted[i - 1];
      if (diff > 1) {
        for (let j: number = 1; j < diff; j++) {
          result.push(numsSorted[i - 1] + j);
        }
      }
    }
  }

  return result;
}

function quickSort(arr: number[]): number[] {
  if (arr.length <= 1) {
    return arr;
  }

  let pivot: number = arr[0];
  let left: number[] = [];
  let right: number[] = [];
  let equals: number[] = [];

  for (let i: number = 0; i < arr.length; i++) {
    if (arr[i] < pivot) {
      left.push(arr[i]);
    } else if (arr[i] > pivot) {
      right.push(arr[i]);
    } else {
      equals.push(arr[i]);
    }
  }

  return [...quickSort(left), ...equals, ...quickSort(right)];
}
