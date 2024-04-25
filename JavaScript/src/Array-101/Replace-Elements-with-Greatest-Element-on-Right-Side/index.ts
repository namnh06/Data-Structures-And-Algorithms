export function replaceElements(arr: number[]): number[] {
  // better solution
  let max: number = arr[arr.length - 1];
  arr[arr.length - 1] = -1;
  for (let i: number = arr.length - 2; i >= 0; i--) {
    let temp: number = arr[i];
    arr[i] = max;
    if (temp > max) {
      max = temp;
    }
  }
  return arr;
  //  original solution
  //   if (arr.length === 0) {
  //     return arr;
  //   }

  //   const lastIndex: number = arr.length - 1;
  //   if (arr.length === 1) {
  //     arr[lastIndex] = -1;
  //     return arr;
  //   }

  //   for (let i: number = 0; i < lastIndex; i++) {
  //     let max: number = arr[i + 1];
  //     for (let j: number = i + 1; j < lastIndex; j++) {
  //       if (max < arr[j + 1]) {
  //         max = arr[j + 1];
  //       }
  //     }
  //     arr[i] = max;
  //   }
  //   arr[lastIndex] = -1;

  //   return arr;
}
