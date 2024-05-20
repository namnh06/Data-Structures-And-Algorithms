export function combineArraysSorted(
  firstArray: number[],
  secondArray: number[]
): number[] {
  const flen: number = firstArray.length;
  const slen: number = secondArray.length;
  let result: number[] = [];
  let i: number = 0;
  let j: number = 0;

  if (flen === 0) {
    return secondArray;
  }

  if (slen === 0) {
    return firstArray;
  }

  while (i < flen && j < slen) {
    if (firstArray[i] <= secondArray[j]) {
      result.push(firstArray[i++]);
    } else {
      result.push(secondArray[j++]);
    }
  }

  while (i < flen) {
    result.push(firstArray[i++]);
  }

  while (j < slen) {
    result.push(secondArray[j++]);
  }

  return result;
}
