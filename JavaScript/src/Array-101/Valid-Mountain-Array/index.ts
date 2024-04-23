export function validMountainArray(arr: number[]): boolean {
  if (arr.length < 3) {
    return false;
  }

  let mid: number = arr[0];
  let pointer: string = "left";
  for (let i = 1; i <= arr.length - 1; i++) {
    if (arr[i] === arr[i - 1] || (i === 1 && arr[i] < arr[i - 1])) {
      return false;
    }

    if (pointer === "left") {
      if (arr[i] > mid) {
        mid = arr[i];
        continue;
      }
      pointer = "right";
    }

    if (pointer === "right") {
      if (arr[i] < mid && arr[i] < arr[i - 1]) {
        if (i === arr.length - 1) {
          return true;
        }
        continue;
      }
      return false;
    }
  }

  return false;
}
