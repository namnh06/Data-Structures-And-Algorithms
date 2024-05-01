export function heightChecker(heights: number[]): number {
  let arrayLength: number = heights.length;
  if (arrayLength <= 1) {
    return 0;
  }

  // sorting array non-decreasing
  let heightsSorted: number[] = quickSort(heights);

  let indices: number = 0;
  // count indices
  for (let index: number = 0; index < arrayLength; index++) {
    if (heightsSorted[index] !== heights[index]) {
      indices++;
    }
  }

  return indices;
}

function quickSort(arr: number[]): number[] {
  if (arr.length < 2) {
    return arr;
  }

  let pivot: number = arr[0];
  let left: number[] = []; // Initialize the 'left' array
  let right: number[] = []; // Initialize the 'right' array
  let equals: number[] = []; // Array to hold elements equal to pivot

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
