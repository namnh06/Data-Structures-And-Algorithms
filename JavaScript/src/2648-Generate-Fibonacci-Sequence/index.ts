export function* fibGenerator(): Generator<number, any, number> {
  let current: number = 0;
  let next: number = 1;
  while (true) {
    yield current;
    [current, next] = [next, current + next];
  }
}
