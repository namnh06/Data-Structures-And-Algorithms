export function combineArraysSorted(
  firstArray: number[],
  secondArray: number[]
): number[] {
  const flen: number = firstArray.length;
  const slen: number = secondArray.length;
  let result: number[] = [];

  if (flen === 0) {
    return secondArray;
  }

  if (slen === 0) {
    return firstArray;
  }

  let pointer: number = 0;
  while (pointer < flen && pointer < slen) {
    if (firstArray[pointer] <= secondArray[pointer]) {
      result.push(firstArray[pointer]);
      result.push(secondArray[pointer++]);
    } else {
      result.push(secondArray[pointer]);
      result.push(firstArray[pointer++]);
    }
  }

  while (pointer < flen) {
    result.push(firstArray[pointer++]);
  }

  while (pointer < slen) {
    result.push(firstArray[pointer++]);
  }

  return result;
}
