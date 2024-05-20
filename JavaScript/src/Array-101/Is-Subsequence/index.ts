export function isSubsequence(s: string, t: string): boolean {
  const slen: number = s.length;
  const tlen: number = t.length;
  let i: number = 0;
  let j: number = 0;

  while (i < slen && j < tlen) {
    if (s[i] === t[j++]) {
      i++;
    }
  }

  return i === slen;
}
